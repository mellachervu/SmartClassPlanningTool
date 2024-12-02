import requests
from bs4 import BeautifulSoup

def fetch_course_descriptions(url):
    """Fetch course descriptions, prerequisites, and restrictions from the given URL."""
    try:
        # Add a user-agent header to the request to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')
        course_descriptions = {}

        # Locate all course blocks on the page
        course_blocks = soup.find_all('div', class_='courseblock')

        for block in course_blocks:
            # Extract the course code
            code_tag = block.find('span', class_='detail-code')
            course_code = code_tag.find('strong').text.strip() if code_tag else 'Unknown'

            # Extract the course title
            title_tag = block.find('span', class_='detail-title')
            course_title = title_tag.find('strong').text.strip() if title_tag else 'Unknown'

            # Extract the course description
            description_tags = block.find_all('div', class_='courseblockextra')
            descriptions = [desc.text.strip() for desc in description_tags if desc.text.strip()]

            # Combine the descriptions into a single string
            course_description = ' '.join(descriptions) if descriptions else 'No description available'

            # Initialize prerequisites and restrictions
            prerequisites = "No prerequisites listed"
            restrictions = "No restrictions listed"

            # Search through the description tags for prerequisites and restrictions
            for desc in description_tags:
                if "Prerequisite(s):" in desc.text:
                    prerequisites_text = desc.text.split("Prerequisite(s):")[-1].strip()
                    prerequisites = prerequisites_text.replace('\n', ' ').strip()

                if "Restriction(s):" in desc.text:
                    restrictions_text = desc.text.split("Restriction(s):")[-1].strip()
                    restrictions = restrictions_text.replace('\n', ' ').strip()

            # Store course information
            course_descriptions[course_code] = {
                'Title': course_title,
                'Description': course_description,
                'Prerequisites': prerequisites,
                'Restrictions': restrictions
            }
        # print(course_descriptions)
        return course_descriptions

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except Exception as e:
        print(f"Failed to fetch course descriptions: {e}")  # Log other errors

