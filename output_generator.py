import pandas as pd

def export_to_excel(student_info):
    """Export student information and course plans to an Excel file."""
    try:
        output_data = {
            'Student ID': student_info.get('Student ID', ''),
            'Concentration': student_info.get('Concentration', ''),
            'Credits Required': student_info.get('Credits Required', ''),
            'Credits Applied': student_info.get('Credits Applied', ''),
            'Earned Credits': student_info.get('Earned Credits', ''),
            'Still Needed Credits': student_info.get('Still Needed Credits', ''),
            'Still Needed Courses': [],
            'Course Plan': []
        }

        # Prepare Still Needed Courses
        for course in student_info.get('Still Needed Courses', []):
            output_data['Still Needed Courses'].append(
                f"{course['Course Code']} - {course['Course Title']}"
            )

        # Prepare Course Plan
        for course in student_info.get('Course Plan', []):
            output_data['Course Plan'].append(
                f"{course['Course Code']} - {course['Course Title']} "
                f"({course.get('Semesters Available', 'Not Available')} - "
                f"Prerequisites: {course.get('Prerequisites', 'No prerequisites listed')} - "
                f"Description: {course.get('Description', 'No description available')})"
            )

        # Create DataFrame
        df = pd.DataFrame({key: pd.Series(value) for key, value in output_data.items()})

        # Export to Excel
        output_path = 'student_info_output.xlsx'
        df.to_excel(output_path, index=False)
        return output_path

    except Exception as e:
        raise RuntimeError(f"Failed to export data to Excel: {e}")
