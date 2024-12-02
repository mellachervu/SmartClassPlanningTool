import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# Define the updated course data
courses = {
    'Semester 1': [
        {'Course Code': 'CS101', 'Course Name': 'Introduction to Computer Science', 'Credits': 3, 'Prerequisites': 'None'},
        {'Course Code': 'MATH101', 'Course Name': 'Calculus I', 'Credits': 4, 'Prerequisites': 'None'},
        {'Course Code': 'ENG101', 'Course Name': 'English Composition', 'Credits': 3, 'Prerequisites': 'None'},
        {'Course Code': 'HIST101', 'Course Name': 'World History I', 'Credits': 3, 'Prerequisites': 'None'},
    ],
    'Semester 2': [
        {'Course Code': 'CS102', 'Course Name': 'Data Structures', 'Credits': 4, 'Prerequisites': 'CS101'},
        {'Course Code': 'MATH102', 'Course Name': 'Calculus II', 'Credits': 4, 'Prerequisites': 'MATH101'},
        {'Course Code': 'PHYS101', 'Course Name': 'Physics I', 'Credits': 4, 'Prerequisites': 'MATH101'},
        {'Course Code': 'ENG102', 'Course Name': 'English Literature', 'Credits': 3, 'Prerequisites': 'ENG101'},
    ],
    'Semester 3': [
        {'Course Code': 'CS201', 'Course Name': 'Algorithms', 'Credits': 3, 'Prerequisites': 'CS102'},
        {'Course Code': 'CS202', 'Course Name': 'Computer Architecture', 'Credits': 4, 'Prerequisites': 'CS102'},
        {'Course Code': 'MATH201', 'Course Name': 'Linear Algebra', 'Credits': 3, 'Prerequisites': 'MATH102'},
        {'Course Code': 'PHYS102', 'Course Name': 'Physics II', 'Credits': 4, 'Prerequisites': 'PHYS101'},
    ],
    'Semester 4': [
        {'Course Code': 'CS301', 'Course Name': 'Operating Systems', 'Credits': 4, 'Prerequisites': 'CS201'},
        {'Course Code': 'CS302', 'Course Name': 'Database Systems', 'Credits': 4, 'Prerequisites': 'CS201'},
        {'Course Code': 'MATH202', 'Course Name': 'Discrete Mathematics', 'Credits': 3, 'Prerequisites': 'MATH201'},
        {'Course Code': 'ECON101', 'Course Name': 'Microeconomics', 'Credits': 3, 'Prerequisites': 'None'},
    ]
}


# Convert the courses dictionary into a DataFrame
def courses_to_dataframe(courses):
    data = []
    for semester, course_list in courses.items():
        for course in course_list:
            course_info = {
                'Semester': semester,
                'Course Code': course['Course Code'],
                'Course Name': course['Course Name'],
                'Credits': course['Credits'],
                'Prerequisites': course['Prerequisites']
            }
            data.append(course_info)
    return pd.DataFrame(data)

# Generate the DataFrame
df_courses = courses_to_dataframe(courses)


# Function to display the course data in a dropdown and download the Excel file
def display_courses_and_download():
    dropdown = widgets.Dropdown(
        options=list(courses.keys()),
        description='Select Semester:',
        disabled=False,
    )

    output = widgets.Output()

    def on_dropdown_change(change):
        with output:
            output.clear_output()
            semester_courses = df_courses[df_courses['Semester'] == change['new']]
            display(semester_courses)

    dropdown.observe(on_dropdown_change, names='value')

    download_button = widgets.Button(description='Download Excel')

    def download_excel(b):
        excel_filename = 'courses_schedule.xlsx'
        df_courses.to_excel(excel_filename, index=False)
        from google.colab import files
        files.download(excel_filename)  # This line allows you to download the file

    download_button.on_click(download_excel)

    display(dropdown, output, download_button)

# Call the function to create the UI
display_courses_and_download()
