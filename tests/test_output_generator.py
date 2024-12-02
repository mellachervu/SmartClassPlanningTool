import pytest
from output_generator import export_to_excel

def test_export_to_excel():
    student_info = {
        'Student ID': '123456',
        'Concentration': 'Computer Science',
        'Credits Required': 30,
        'Credits Applied': 21,
        'Earned Credits': '15',
        'Still Needed Credits': '6',
        'Completed Courses': [{'Course Code': 'CPSC 1101', 'Course Title': 'Intro to Programming'}],
        'Still Needed Courses': [{'Course Code': 'CPSC 1102', 'Course Title': 'Data Structures'}],
        'Course Plan': [{'Course Code': 'CPSC 1102', 'Course Title': 'Data Structures', 'Semesters Available': 'Fall, Spring'}]
    }
    output_path = export_to_excel(student_info)
    assert output_path == 'student_info_output.xlsx'