from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Users/xu35k6jo6/Desktop/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://cmap.cycu.edu.tw:8443/MyMentor/courseCreditStructure.do")
print(driver.text)
# studentnumber = driver.find_element_by_id("userId")
# password = driver.find_element_by_id("password")
# login = driver.find_element_by_id("loginImg")

# studentnumber.clear()
# password.clear()

# studentnumber.send_keys("10811245")
# password.send_keys("Qqpr0518")
# login.click()
