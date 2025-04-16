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

    

#Get lesson plan page content and create a soup
page = requests.get(lesson_url, headers=headers)
soup = BeautifulSoup(page.content, features='lxml')

#Extracting the data from page section
"""This is where I have to view the HTML code of the webpage.
I can use the inspect tool in the browser to view the HTML code.
Alternatively I can choose Inspect to access the Developer tools and make sure I'm in the Elements tab to see the HTML structure."""

#Extracting title of lesson plan
lesson_title = soup.find('div', class="small-12 medium-9 columns")
if lesson_title:
    title_element = title_div.find('h2')
    if title_element:
        title = title_element.text.strip()
        lesson_plans['title'] = title

#Extracting Subjects of lesson plan
subjects = soup.find('div', class="small-12 columns")
if subjects:
    subject_element = subjects.find('p')
    if subject_element:
        subject = subject_element.text.strip()
        lesson_plans['subject'] = subject