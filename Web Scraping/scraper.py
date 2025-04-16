### Web Scraping file to Teacher Resources ###

import requests
from bs4 import BeautifulSoup

headers = {
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'
  'Accept-Language' : 'en-US,en;q=0.5'
}


def get_lesson_plans(lesson_url: str) -> dict:
    #Create an empty lesson plan details dictionary
    lesson_plans = {}

    page = requests.get(lesson_url, headers=headers)
    soup = BeautifulSoup(page.content, features='lxml')

    try:
        #Extracting title of lesson plan
        lesson_title = soup.find('div', class="small-12 medium-9 columns")
        if lesson_title:
            title_element = lesson_title.find('h2')
            if title_element:
                title = title_element.text.strip()

        #Extracting Subjects of lesson plan
        subjects = soup.find('div', class="small-12 columns")
        if subjects:
            subject_element = subjects.find('p')
            if subject_element:
                subject = subject_element.text.strip()

        #Adding data to the lesson plan dictionary
        lesson_plans['title'] = title
        lesson_plans['subject'] = subject

        #Return the lesson plan dictionary
        return lesson_plans
    except Exception as e:
        print("Error: Unable to retrieve lesson plan details.")
        print(f'Failed with exception: {e}')
    
#Prompting user
product_url = input("Enter the URL of the lesson plan: ")
lesson_plans = get_lesson_plans(product_url)

print(lesson_plans)

    

