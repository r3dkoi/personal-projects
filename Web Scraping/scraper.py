### Web Scraping file to Teacher Resources ###

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept-Language': 'en-US,en;q=0.5'
}


def get_lesson_plans(lesson_url: str) -> dict:
    # Create an empty lesson plan details dictionary
    lesson_plans = {
        'title': 'Not found',
        'subject': 'Not found'
    }

    try:
        # Get the page content
        page = requests.get(lesson_url, headers=headers)
        page.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(page.content, features='lxml')

        # Extracting title of lesson plan
        lesson_title = soup.find('div', class_="small-12 medium-9 columns")
        if lesson_title:
            title_element = lesson_title.find('h2')
            if title_element:
                lesson_plans['title'] = title_element.text.strip()

        # Extracting Subjects of lesson plan 
        """Will need to revise this as the div is encompasses multiple paragraphs and I need to just specify specific <p> tags that contains the subjects."""
        subjects = soup.find('div', class_="small-12 columns")
        if subjects:
            subject_element = subjects.find('p')
            if subject_element:
                lesson_plans['subject'] = subject_element.text.strip()

        return lesson_plans
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to retrieve the webpage. {e}")
        return lesson_plans
    except Exception as e:
        print("Error: Unable to retrieve lesson plan details.")
        print(f'Failed with exception: {e}')
        return lesson_plans


# Main execution block
if __name__ == "__main__":
    try:
        # Prompting user
        product_url = input("Enter the URL of the lesson plan: ")
        lesson_plans = get_lesson_plans(product_url)
        print(lesson_plans)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
