# SmartClass Planning Tool

## Purpose

The **SmartClass Planning Tool** is an intelligent software system designed to assist students and academic advisors in managing course planning for university programs. It provides students with a detailed course schedule, tracks earned and remaining credits, and helps in course selection based on prerequisites. The tool also generates a course plan for the upcoming semesters based on student progress and program requirements.

## Prerequisites

Before using the **SmartClass Planning Tool**, ensure that you have the following prerequisites:

- **Python 3.7+** installed on your system.
- The following Python packages:
    - `pandas` (for data processing)
    - `openpyxl` (for Excel file handling)
    - `PyPDF2` (for reading PDF files)
    - `requests` (for web scraping)
    - `beautifulsoup4` (for parsing HTML content)
  
You can install these dependencies using the provided `requirements.txt` file.

## Download

You can download the source code and installer for the **SmartClass Planning Tool** from the following links:

- https://github.com/mellachervu/SmartClassPlanningTool
- https://github.com/mellachervu/SmartClassPlanningTool/blob/master/SmartClassPlanningTool.exe

Alternatively, you can download the files directly using the provided links.

## Build/Configuration/Installation/Deployment

### Step 1: Clone or Download the Source Code

Download or clone the source code to your local machine.

### Step 2: Install Dependencies

1. Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

2. Install the required dependencies using pip:

pip install -r requirements.txt

3. Running the Application:

Ensure you have all the necessary input files (e.g., DegreeWorks.pdf, four_year_schedule.xlsx, etc.).
To run the main program, execute the following command:

python main.py

4. Generating Output:

The program will process the required inputs and generate an output file (e.g., student_info_output.xlsx) containing the course plan, student progress, and other relevant data.

## Usage

How to Use the SmartClass Planning Tool
1. Input Files: Ensure that you have the required files in the same directory:

DegreeWorks PDF: This is your student's DegreeWorks report (typically a PDF file).
Four-Year Schedule Excel File: A schedule of available courses in Excel format.
Graduate Study Plans Excel File: Contains information about course prerequisites and schedules.

2. Run the Program: Once the input files are available, you can simply run the program using the following command:

python main.py

3. Generated Output: After the program runs, an output Excel file will be generated with the following details:

Completed Courses
Still Needed Courses
Course Plan for upcoming semesters

4. Viewing the Results: The output will be saved in an Excel file (student_info_output.xlsx). You can open this file to review the student's academic progress and course planning.

## Installer Set Up

1. For installation, unzip the project folder.
2. Install Inno Setup software on the pc.
3. After installation of Inno Setup, Open it and select a new script.
4. A dialogue box appears, please add the necessary information.
5. Load the project in the Inno Setup Wizard box.
6. Compile it.
7. After compilation, the desired application should be running.

**License**
The SmartClass Planning Tool is open-source software. Feel free to use and modify it according to your needs.
