import pytest
from web_crawler import fetch_course_descriptions

def test_fetch_course_descriptions():
    url = 'https://catalog.columbusstate.edu/course-descriptions/cpsc/'
    descriptions = fetch_course_descriptions(url)
    assert isinstance(descriptions, dict)  # Expecting a dictionary
    assert 'CPSC 1105' in descriptions  # Example course code
