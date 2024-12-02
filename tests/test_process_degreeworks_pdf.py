import pytest
from process_degreeworks_pdf import process_degreeworks_pdf

def test_process_degreeworks_pdf():
    student_info = process_degreeworks_pdf('C:/Users/manid/PycharmProjects/SmartClassPlanningTool/inputs/DegreeWorks.pdf', 'C:/Users/manid/PycharmProjects/SmartClassPlanningTool/inputs/four_year_schedule.xlsx', 'C:/Users/manid/PycharmProjects/SmartClassPlanningTool/inputs/Graduate_Study_Plans_revised.xlsx', 'https://catalog.columbusstate.edu/course-descriptions/cpsc/')
    assert student_info['Student ID'] == '909487472'
    assert student_info['Concentration'] == 'General Computer Science'
