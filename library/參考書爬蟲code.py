from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
PATH = "C:/Users/xu35k6jo6/Desktop/chromedriver.exe"
driver = webdriver.Chrome(PATH)
Courses = pd.read_csv('C:\python-training\Courses.csv')

with open( "參考書.csv", mode = "w",encoding = "utf-8" ) as file:
    file.write("課程代碼,參考書1,參考書2\n")

for course in Courses['課程代碼']:
    url = "https://cmap.cycu.edu.tw:8443/Syllabus/CoursePreview.html?yearTerm=1102&opCode=" + str(course)

    driver.get(url) #進此網站
#   教科書Xpath
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[13]/td/table/tbody/tr[2]/td[1]/div
#   參考書Xpath
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[11]/td[1]/div
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[4]/td[1]/div
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[2]/td[1]/div
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[1]/td/div
    bookline = 3
    book1 = driver.find_elements_by_xpath('//*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[' +str(bookline)+ ']/td[1]/div')


    # # Get scroll height
    # last_height = driver.execute_script("return document.body.scrollHeight")

    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #     # Wait to load page
    #     time.sleep(SCROLL_PAUSE_TIME)

    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height
    line = 0

    
    with open( "參考書.csv", mode = "a",encoding = "utf-8" ) as file:
        file.write( course )
    for book1s in book1:
        line = 1
        with open( "參考書.csv", mode = "a",encoding = "utf-8" ) as file:
            file.write(  ',' +  '\"' + book1s.text + '\"')
    bookMore2 = 0
    while len(book1) != 0 : 
        bookMore2 = 1
        bookline +=1
        book1 = driver.find_elements_by_xpath('//*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[' +str(bookline)+ ']/td[1]/div')
        for book1s in book1:
            line = 1
            with open( "參考書.csv", mode = "a",encoding = "utf-8" ) as file:
                file.write(  ',' +  '\"' + book1s.text + '\"')
    if bookMore2 != 0:
        with open( "參考書.csv", mode = "a",encoding = "utf-8" ) as file:
            file.write( "\n")
          
        
    if line != 1:
        with open( "參考書.csv", mode = "a",encoding = "utf-8" ) as file:
            file.write( '\n' )

        
time.sleep(10)
driver.quit()


