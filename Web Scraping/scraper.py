### Web Scraping file to Teacher Resources ###

import requests
from bs4 import BeautifulSoup

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'
  'Accept-Language': 'en-US,en;q=0.5'
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
"""Since the website I'm currently trying to scrape has their lesson plan data inside a href, I needed to use 
the lambda function to find an anchor with the href starting with the '/lessons/'"""
title_element = soup.find('a', href=lambda href: href and href.startswidth('/lessons/') 
                          if title_element:
                            title = title_element.text.strip() #Takes the text from the title element and removes any leading or trailing whitespace
                            lessons_plans['title'] = title) #Places extracted title into the lesson_plans dictionary

#Extracting Grades of lesson plan
grades_element = soup.find('td', string=lambda text:text and 'Grades' in text)
if grades_element:
    grades = grades.element.text.strip()
    lesson_plans['grades'] = grades #Places extracted grades data into the lesson_plans dictionary
    
#Extracting Subjects of lesson plan
subjects_element = soup.find('td', string=lambda )
