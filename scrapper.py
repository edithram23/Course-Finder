# """I have used selenium to 
# webscrap the free courses from the webpage."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
def scrape_free_courses(driver, url,data,link):
    driver.get(url)
    # Wait until the course list is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'products__list'))
    )
    courses = driver.find_elements(By.CLASS_NAME, 'products__list-item')
    
    for course in courses:
        title_element = course.find_element(By.TAG_NAME, 'h3')
        course_title = title_element.text.strip()
        
        # Check if the course is free by looking for the 'Free' label
        try:
            price_element = course.find_element(By.CLASS_NAME, 'course-card__price')
            price_text = price_element.text.strip()
            # print(price_text)
            if 'Free' in price_text:
                # print(course_title)
                course_link = course.find_element(By.TAG_NAME, 'a').get_attribute('href')
                # print(course_link)
                data+=[course_title]
                link+=[course_link]
            else:
                print(course_title)
        except:
            print(course_title)
            continue
    return data,link

def scrape_course_content(driver, course_url):
    driver.get(course_url)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main.course"))
        )
        # Find the <main> tag and extract all the content inside
        main_content = driver.find_element(By.CSS_SELECTOR, "main.course")
        course_content = main_content.text.strip()
        # print(course_content)
        return course_content
    except:
        print(course_url)
        return ''

driver = webdriver.Edge()
df = pd.DataFrame()

urls=[]
for i in range(1,9):
    url = f'https://courses.analyticsvidhya.com/collections/courses?page={i}'
    urls+=[url]
    
data=[]
link=[]
for url in urls:
    data,link=scrape_free_courses(driver, url,data,link)

df['Course_Name']=data
df['Course_Link']=link
df.to_csv("Course.csv") #consisting only links and course names

content=[]
for course_url in link:
    content+=[scrape_course_content(driver, course_url)]
df['Content']=content

df.to_csv('Courses_content.csv')
driver.quit()