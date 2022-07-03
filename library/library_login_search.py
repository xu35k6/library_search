from plistlib import UID
from unittest.util import unorderable_list_difference
from numpy import uint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
#import pyautogui
print(__name__)
url = "https://jumper.lib.cycu.edu.tw/cycu/jumper/index.jsp"
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

#登入
id = input('請輸入學號或帳號:')
Password = input("請輸入密碼:")
uid = driver.find_element(By.ID,"uid")
uid.send_keys(id)
password = driver.find_element(By.ID,"pwd")
password.send_keys(Password,Keys.ENTER)

#跳轉頁面後
WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "description_fullsearch"))
    )
#搜尋
search = driver.find_element(By.ID,'textfield')
search.clear()
Bookname = input("請輸入書名:")
search.send_keys(Bookname,Keys.ENTER)
#搜尋完跳轉頁面後
WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "filterkey"))
    )

#搜尋作者
Author = input("請輸入作者:")
author_search = driver.find_element(By.XPATH,'//*[@id="filterkey"]')
author_search.send_keys(Author,Keys.ENTER)

author_search_btn = driver.find_element(By.XPATH,'//*[@id="filterkeyDiv"]/div/input[2]')
author_search_btn.click()

#搜尋年代
book_era = driver.find_element(By.XPATH,'//*[@id="range_syear"]')
year = input("請輸入搜尋開始的年代:")
lastyear = input("請輸入搜尋截止的年代:")
book_era.send_keys( str(int(year)-1) + '12', Keys.TAB, str(int(lastyear)) + '12')

book_era_btn = driver.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr/td[1]/div[4]/div/input[8]')
book_era_btn.click()

#TODO
#  書的架上情況是依據個別書的ID去存取的 目前無法統一爬取
# WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.ID, "1952687_msg"))
#     )

# book_stock = driver.find_elements(By.ID,'1952687_msg')
# for book in book_stock:
#     print(book.text)
    

# print('15')
# pyautogui.hotkey('ctrl', 'tab', interval=0.1)
#driver.quit()

