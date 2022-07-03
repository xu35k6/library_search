from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
#chromdriver設定:先下載chromdriver
PATH = "C:/Users/xu35k6jo6/Desktop/chromedriver.exe" #chromdriver於電腦的位置
driver = webdriver.Chrome(PATH)
Courses = pd.read_csv('C:\python-training\Courses.csv') #讀取課程代碼

with open( "教科書.csv", mode = "w",encoding = "utf-8" ) as file:
    file.write("課程代碼,教科書1,教科書2\n")

for course in Courses['課程代碼']:
    url = "https://cmap.cycu.edu.tw:8443/Syllabus/CoursePreview.html?yearTerm=1102&opCode=" + str(course) #設定讀取網址
    driver.get(url) #進此網站

#   教科書Xpath
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[13]/td/table/tbody/tr[2]/td[1]/div
#   參考書Xpath
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[11]/td[1]/div
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[4]/td[1]/div
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[2]/td[1]/div
#                                         //*[@id="coursepreview"]/div/div[2]/table/tbody/tr[14]/td/table/tbody/tr[1]/td/div
    bookline = 3

    #設定第一本書的爬取位置(xpath)
    book1 = driver.find_elements_by_xpath('//*[@id="coursepreview"]/div/div[2]/table/tbody/tr[13]/td/table/tbody/tr[' +str(bookline)+ ']/td[1]/div')

    line = 0 # 如果有教科書的話 = 1 

#先讀取課程代碼
    with open( "教科書.csv", mode = "a",encoding = "utf-8" ) as file:
        file.write( course )

#先讀取第一本書
    for book1s in book1:
        line = 1
        with open( "教科書.csv", mode = "a",encoding = "utf-8" ) as file:
            file.write(  ',' +  '\"' + book1s.text + '\"')

    bookMore2 = 0#超過一本書的話 = 1

#如果有第一本書 爬取下一本書
    while len(book1) != 0 : 
        bookMore2 = 1
        bookline +=1
        #令book1 = 下一本書
        book1 = driver.find_elements_by_xpath('//*[@id="coursepreview"]/div/div[2]/table/tbody/tr[13]/td/table/tbody/tr[' +str(bookline)+ ']/td[1]/div')
        for book1s in book1:
            line = 1
            with open( "教科書.csv", mode = "a",encoding = "utf-8" ) as file:
                file.write(  ',' +  '\"' + book1s.text + '\"')

#讀取完所有書後換行                
    if bookMore2 != 0:
        with open( "教科書.csv", mode = "a",encoding = "utf-8" ) as file:
            file.write( "\n")
          
#沒有書直接換行
    if line != 1:
        with open( "教科書.csv", mode = "a",encoding = "utf-8" ) as file:
            file.write( '\n' )

        
time.sleep(10)
driver.quit()


