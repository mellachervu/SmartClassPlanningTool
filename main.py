import os
import json
from process_degreeworks_pdf import process_degreeworks_pdf
from output_generator import export_to_excel


def load_config():
    """Load configuration from config.json."""
    if not os.path.exists('config.json'):
        raise FileNotFoundError("Configuration file 'config.json' not found.")

    with open('config.json', 'r') as file:
        config = json.load(file)

    return config


def main():
    try:
        # Load configuration
        config = load_config()

        # Process the DegreeWorks PDF
        student_info = process_degreeworks_pdf(
            config['pdf_path'],
            config['schedule_path'],
            config['plans_path'],
            config['course_desc_url']
        )

        # Export the processed information to Excel
        output_path = export_to_excel(student_info)
        print(f"Student information has been exported to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
