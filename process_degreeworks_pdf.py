import re
import os
import pandas as pd
from PyPDF2 import PdfReader
from web_crawler import fetch_course_descriptions

def process_graduate_study_plans(plans_path):
    try:
        df = pd.read_excel(plans_path)
        courses = []
        for index, row in df.iterrows():
            if pd.notna(row['Course Number']):
                courses.append({
                    'Course Code': row['Course Number'].strip(),
                    'Course Title': row['Course name'].strip()
                })
        return courses
    except Exception as e:
        raise RuntimeError(f"Failed to process Graduate Study Plans: {e}")


def process_four_year_schedule(schedule_path):
    """Process the 4-Year Schedule from an Excel file."""
    try:
        df = pd.read_excel(schedule_path, header=2)  # Read the Excel file

        # Get only the unhidden columns
        df = df.iloc[:, :2].join(df.iloc[:, 13:])
        # Extract terms dynamically from the DataFrame columns
        terms = df.columns[2:]  # Assuming the first two columns are Course and Course Title

        schedule = []
        for index, row in df.iterrows():
            course_code = row['Course'].strip() if isinstance(row['Course'], str) else None
            course_title = row['Course Title'].strip() if isinstance(row['Course Title'], str) else None

            if course_code and course_title:
                for term in terms:  # Iterate over dynamic terms
                    if pd.notna(row[term]) and row[term] != "":
                        schedule.append({
                            'Semester': term.strip(),  # Clean up the term name
                            'Course Code': course_code,
                            'Course Title': course_title
                        })
        return schedule
    except Exception as e:
        raise RuntimeError(f"Failed to process Four-Year Schedule: {e}")

def extract_semesters(course_code, schedule):
    available_semesters = [entry['Semester'] for entry in schedule if entry['Course Code'] == course_code]
    return ', '.join(available_semesters) if available_semesters else "Not Offered"

def process_degreeworks_pdf(pdf_path, schedule_path, plans_path, course_desc_url):
    try:
        # Fetch course descriptions from the web
        course_descriptions = fetch_course_descriptions(course_desc_url)
        graduate_study_plans = process_graduate_study_plans(plans_path)
        print(graduate_study_plans)
        four_year_schedule = process_four_year_schedule(schedule_path)

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"DegreeWorks PDF file not found: {pdf_path}")

        reader = PdfReader(pdf_path)
        # text = " ".join(line for page in reader.pages for line in page.extract_text().splitlines() if line)
        text = " ".join(line.strip() for page in reader.pages for line in page.extract_text().splitlines() if line.strip())

        student_info = {}

        # Extract Name
        name_match = re.search(r"Student ID\s+(\d+)", text)
        student_info['Student ID'] = name_match.group(1).strip() if name_match else 'Unknown'


        # Extract Concentration
        concentration_match = re.search(r"Concentration\s+([A-Za-z\s&-]+)", text)
        student_info['Concentration'] = concentration_match.group(1).strip() if concentration_match else 'Unknown'

        # Extract Earned Credits
        earned_match = re.search(r'Earned Credits\s+(\d+)', text)
        student_info['Earned Credits'] = earned_match.group(1).strip() if earned_match else '0'

        # Extract Credits Required and Applied
        credits_required_match = re.search(r"Credits required:\s*(\d+)", text)
        required_credits = int(credits_required_match.group(1).strip()) if credits_required_match else 0
        credits_applied_match = re.search(r"Credits applied:\s*(\d+)", text)
        credits_applied = int(credits_applied_match.group(1).strip()) if credits_applied_match else 0
        student_info['Credits Required'] = credits_required_match.group(1).strip() if credits_required_match else '0'
        student_info['Credits Applied'] = credits_applied_match.group(1).strip() if credits_applied_match else '0'

        # Calculate Still Needed Credits
        student_info['Still Needed Credits'] = required_credits - credits_applied

        text = " ".join(page.extract_text() for page in reader.pages)
        # Extract Still Needed Courses
        still_needed_courses = []
        still_needed_course_matches = re.findall(r"([A-Z]{4}\s*\d{4})-\s*([A-Za-z\s&-]+)(Still needed:.*)", text)

        for course in still_needed_course_matches:
            course_code = course[0].strip()
            course_title = re.sub(r'Still needed.*', '', course[1]).strip()
            still_needed_courses.append({
                'Course Code': course_code,
                'Course Title': course_title,
            })

        student_info['Still Needed Courses'] = still_needed_courses

        # Generate Course Plan based on still needed courses, prerequisites from course descriptions, and course descriptions
        student_info['Course Plan'] = []
        for course in still_needed_courses:
            course_code = course['Course Code']
            course_description = course_descriptions.get(course_code, {})
            prerequisites = course_description.get('Prerequisites', 'No prerequisites listed')
            student_info['Course Plan'].append({
                'Course Code': course_code,
                'Course Title': course['Course Title'],
                'Semesters Available': extract_semesters(course_code, four_year_schedule),
                'Prerequisites': prerequisites,
                'Description': course_description.get('Description', 'No description available')
            })

        # Include graduate study plans that apply
        student_info['Applicable Graduate Plans'] = [
            plan for plan in graduate_study_plans if plan['Course Code'] in student_info['Still Needed Courses']
        ]

        return student_info

    except Exception as e:
        raise RuntimeError(f"Error processing DegreeWorks PDF: {e}")
