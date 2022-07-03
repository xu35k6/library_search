from cmath import nan
from pdb import line_prefix
from plistlib import UID
from pydoc import pager
from ssl import Purpose
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
import os,sys
import pandas as pd
import datetime
#import pyautogui
haveclass = False
start = time.time()
try:
    purpose = input("請問您想找參考書還是教科書呢?")
    #C:\python\圖書館搜尋\教科書(含名稱).csv
    booknum = pd.read_csv('C:\python\圖書館搜尋\\'+ purpose + '(含名稱).csv')
    classnum = input("請輸入您想搜尋的課程代碼:")
    find = False
    i = 1
    # for Booknum,Book in zip(booknum["課程代碼"],booknum[purpose + '1']) :
    #     if classnum == Booknum:
    #         searchpurpose = Book
    #         find = True
    #         break
    for Booknum,Book in zip(booknum["課程代碼"],booknum[purpose + '1']) :
        i +=1
        j = 1
        if classnum == Booknum:
            find = True
            print("已為您搜尋:",booknum['課程名稱'][i-2])
            if str(booknum[purpose+ str(j)][i-2]) != 'nan' and j<41:
                print("以下為教授提供的"+purpose+'清單:')
                while str(booknum[purpose+ str(j)][i-2]) != 'nan' and j<41:
                    print(j,":",booknum[purpose+ str(j)][i-2])
                    j+=1
                j = input('請問您想搜尋第幾本書呢?')
                searchpurpose = booknum[purpose + str(j)][i-2]
            break

    if str(booknum[purpose+ str(j)][i-2]) == 'nan' and  find:
        print("老師沒公布"+ purpose +"QQ")
    elif find:
        haveclass = True
        print("老師公布的"+ purpose +"為:"+ str(searchpurpose) + '\n已為您搜尋--------')
#selenium
        url = "https://cylis.lib.cycu.edu.tw/"
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        

#搜尋


        book_search = driver.find_element(By.NAME,'searcharg')
        book_search.send_keys('t:('+ str(searchpurpose) +')',Keys.ENTER)

        # try:
        #     WebDriverWait(driver, 5).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, 'srchhelpText'))
            
        #     )
        mode = 1
        # except:
        #     print("找不到書")
        #     mode = 3
        # if mode != 3:
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="rightSideCont"]/table[1]/tbody/tr[1]/td/div/form/div[2]/input'))
            )
            E_Books = input("需要限制為可外借藏館嗎?(Y\\N):")
            start2 = time.time()
            start = start2
            if E_Books == 'Y':
                e_books = driver.find_element(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[1]/td/div/form/div[2]/input')
                e_books.click()
                search_btn = driver.find_element(By.NAME,'SUBMIT')
                search_btn.click()
        except:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="bibDisplayContent"]/div[1]/form/div[2]/input'))
            )
            E_Books = input("需要限制為可外借藏館嗎?(Y\\N):")    
            if E_Books == 'Y':
                e_books = driver.find_element(By.XPATH,'//*[@id="bibDisplayContent"]/div[1]/form/div[2]/input')
                e_books.click()
                search_btn = driver.find_element(By.NAME,'SUBMIT')
                search_btn.click()       
        #查詢完成頁面跳轉後
        #XXX:會卡5~10秒 非必要
        try:
            WebDriverWait(driver, 5).until(#                  //*[@id="bibDisplayContent"]/div[1]/div/i[1]
                    EC.presence_of_element_located((By.CLASS_NAME, 'bibSearchtoolMessage'))
                )
            result = driver.find_elements(By.CLASS_NAME,'bibSearchtoolMessage')
            for Result in result:
                print('共',Result.text)
        except:
            WebDriverWait(driver, 5).until(#                  //*[@id="bibDisplayContent"]/div[1]/div/i[1]
                    EC.presence_of_element_located((By.CLASS_NAME, 'browseSearchtoolMessage'))
                )
            result = driver.find_elements(By.CLASS_NAME,'browseSearchtoolMessage')
            for Result in result:
                print('共',Result.text)

            

        #判斷讀者搜尋的書是否僅有一本 一本的話mode為1 兩本或以上mode為2
        if mode!=3:
            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "bibInfoData"))
                )
                mode = 1

            except:
                mode = 2
        # print('MODE=',mode)
        #僅有一本
        if mode == 1:
            line = 2
            booknameline = 1
            findbooknameline = True
            onlyonebook = driver.find_elements(By.XPATH,'//*[@id="bibDisplayLayout"]/tbody/tr/td[1]/table[1]/tbody/tr/td/table/tbody/tr['+ str(booknameline)+']/td[1]')
            for firstbook in onlyonebook:
                while(findbooknameline):
                    onlyonebook = driver.find_elements(By.XPATH,'//*[@id="bibDisplayLayout"]/tbody/tr/td[1]/table[1]/tbody/tr/td/table/tbody/tr['+ str(booknameline)+']/td[1]')
                    for Firstbook in onlyonebook:
                        if Firstbook.text == '書名':
                            findbooknameline = False
                            onlyonebook = driver.find_elements(By.XPATH,'//*[@id="bibDisplayLayout"]/tbody/tr/td[1]/table[1]/tbody/tr/td/table/tbody/tr['+ str(booknameline)+']/td[2]')
                            for Firstbook in onlyonebook:
                                print('您搜尋的藏書只有一本')
                                print('書名:',Firstbook.text) 
                        else:
                            booknameline +=1 

                library = driver.find_elements(By.XPATH,'//*[@id="bibDisplayContent"]/div[4]/table/tbody/tr/td/table[2]/tbody/tr['+ str(line)+']/td[1]')
                booknum = driver.find_elements(By.XPATH,'//*[@id="bibDisplayContent"]/div[4]/table/tbody/tr/td/table[2]/tbody/tr['+ str(line)+']/td[2]')
                booknumber = driver.find_elements(By.XPATH,'//*[@id="bibDisplayContent"]/div[4]/table/tbody/tr/td/table[2]/tbody/tr['+ str(line)+']/td[3]')
                stock = driver.find_elements(By.XPATH,'//*[@id="bibDisplayContent"]/div[4]/table/tbody/tr/td/table[2]/tbody/tr['+ str(line)+']/td[4]')
                for Library,Booknum,Booknumber,Stock in zip(library,booknum,booknumber,stock):
                    havestock = 1
                    print('館藏地:' + '[%-20s]' % Library.text + '，索書號:' + '[%-10s]' %Booknum.text + '，條碼:' + '[%-7s]' %Booknumber.text + '，架上情況:'+ '[%-10s]' %Stock.text + ',')
                    havemore2 = 1
                    while(havemore2 == 1):
                        havemore2 = 0
                        line+=1
                        library = driver.find_elements(By.XPATH,'//*[@id="bibDisplayContent"]/div[4]/table/tbody/tr/td/table[2]/tbody/tr['+ str(line)+']/td[1]')
                        booknum = driver.find_elements(By.XPATH,'//*[@id="bibDisplayContent"]/div[4]/table/tbody/tr/td/table[2]/tbody/tr['+ str(line)+']/td[2]')
                        booknumber = driver.find_elements(By.XPATH,'//*[@id="bibDisplayContent"]/div[4]/table/tbody/tr/td/table[2]/tbody/tr['+ str(line)+']/td[3]')
                        stock = driver.find_elements(By.XPATH,'//*[@id="bibDisplayContent"]/div[4]/table/tbody/tr/td/table[2]/tbody/tr['+ str(line)+']/td[4]')
                        for Library,Booknum,Booknumber,Stock in zip(library,booknum,booknumber,stock):
                            havemore2 = 1
                            print('館藏地:' + '[%-20s]' % Library.text + '，索書號:' + '[%-10s]' %Booknum.text + '，條碼:' + '[%-7s]' %Booknumber.text + '，架上情況:'+ '[%-10s]' %Stock.text + ',')

        #兩本或以上
        elif mode == 2:
            DOIT = True
            num = 1
            while(DOIT):
                line = 3
                #藏書名稱
                book_stockname = driver.find_elements(By.CLASS_NAME,'briefcitTitle')
                #架上情況
                print("以下為圖書館藏書的前五十筆搜尋結果:")
                for Book_stockname in book_stockname:
                    havestock = 0 #有藏書的話=1
                    print('第' + str(num) , '個搜尋結果:' +Book_stockname.text + ':')
                    num+=1
                    library = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[3]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]/td[1]')
                    booknum = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[3]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]/td[2]')
                    booknumber = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[3]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]/td[3]')
                    stock = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[3]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]/td[4]')
                    for Library,Booknum,Booknumber,Stock in zip(library,booknum,booknumber,stock):
                        havestock = 1
                        if havestock == 1:
                            line2 = 2
                            havemore2 = 1
                            while(havemore2 == 1):
                                havemore2 = 0
                                library = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[3]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[' + str(line2) + ']/td[1]')
                                booknum = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[3]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[' + str(line2) + ']/td[2]')
                                booknumber = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[3]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[' + str(line2) + ']/td[3]')
                                stock = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[3]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[' + str(line2) + ']/td[4]')
                                for Library,Booknum,Booknumber,Stock in zip(library,booknum,booknumber,stock):
                                    havemore2 = 1
                                    print('館藏地:' + '[%-20s]' % Library.text + '，索書號:' + '[%-10s]' %Booknum.text + '，條碼:' + '[%-7s]' %Booknumber.text + '，架上情況:'+ '[%-10s]' %Stock.text + ',')
                                if havemore2 == 1:
                                    line2 +=1

                    if havestock == 0 :
                        library = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[2]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]/td[1]')
                        booknum = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[2]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]/td[2]')
                        booknumber = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[2]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]/td[3]')
                        stock = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[2]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]/td[4]')
                        for Library,Booknum,Booknumber,Stock in zip(library,booknum,booknumber,stock):
                            havestock = 1
                            if havestock == 1:
                                line2 = 2
                                havemore2 = 1
                                while(havemore2 == 1):
                                    havemore2 = 0
                                    library = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[2]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[' + str(line2) + ']/td[1]')
                                    booknum = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[2]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[' + str(line2) + ']/td[2]')
                                    booknumber = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[2]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[' + str(line2) + ']/td[3]')
                                    stock = driver.find_elements(By.XPATH,'//*[@id="rightSideCont"]/table[1]/tbody/tr[2]/td/table/tbody/tr[' + str(line) +']/td/table/tbody/tr/td[2]/div[2]/table/tbody/tr[' + str(line2) + ']/td[4]')
                                    for Library,Booknum,Booknumber,Stock in zip(library,booknum,booknumber,stock):
                                        havemore2 = 1
                                        print('館藏地:' + '[%-20s]' % Library.text + '，索書號:' + '[%-10s]' %Booknum.text + '，條碼:' + '[%-7s]' %Booknumber.text + '，架上情況:'+ '[%-10s]' %Stock.text + ',')
                                    if havemore2 == 1:
                                        line2 +=1
                        if havestock == 0:
                            print('這是電子書唷')
                    line+=1

                if num %50 == 1 and num>=50:
                    next = input("需要列出更多搜尋結果嗎?(Y\\N)")
                    if next == 'Y':
                        DOIT = True
                        nextpage = driver.find_element(By.XPATH,'//*[@id="id_icon_paging_prev"]')
                        nextpage.click()
                    else: 
                        DOIT = False
                else:
                    DOIT = False
        #找不到
        else :
            print("抱歉><搜尋不到你想找的書")
        print("謝謝使用唷!!")
        driver.quit()

    else:
        print('沒有這堂課QQ')
except:
    if haveclass:
        print('圖書館目前無符合的藏書QQ')
    else:
        if purpose != '參考書' and purpose != '教科書':
            print("輸入錯誤~!!!")
        else:
            print("找不到這門課QQ")

end = time.time()
print(end-start)