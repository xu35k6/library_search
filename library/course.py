from sre_constants import JUMP
import pandas as pd
import requests
import re
from fake_useragent import UserAgent
import random
import time
import openpyxl
import xlsxwriter
ua = UserAgent()

headerlist = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
              "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
              "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
              "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]

url = "https://itouch.cycu.edu.tw/active_system/CourseQuerySystem/"
requ = requests.get(url, headers = {
    "user_agent" : random.choice(headerlist)
})
rejs = requ.json()
pd.DataFrame(
        data=
        [{'老師':rejs['TEACHER_CNAME'],
          '必選修/期程/學分':rejs['OP_STDY_AND_OP_QUALITY_AND_OP_CREDIT'],
          '開課系級':rejs['DEPT_ABVI_C'],
          '課程類別':rejs['OP_TYPE'],
          '課程名稱':rejs['c.CURS_NM_C_S'],}],
        columns=['老師','必選修/期程/學分','開課系級','課程類別','課程名稱'])
