import time
from datetime import datetime
from email.utils import format_datetime
from os import fsdecode

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/Dynamic table and windows.html")
time.sleep(2)
No_of_rows=driver.find_elements(By.XPATH,"//*[@id='stockTable']/tbody/tr")
print("No of rows present",len(No_of_rows))
No_of_columns=driver.find_elements(By.XPATH,"//*[@id='stockTable']/thead/tr/th")
print("No of columns present",len(No_of_columns))
lis=[]
for i in range(1,len(No_of_columns)+1):
    ele=driver.find_element(By.XPATH,"//*[@id='stockTable']/tbody/tr["+str(i)+"]/td[3]")
    #print(ele.text)
    ele1=ele.text.split("$")
    #lis.append((i,float(ele1[1])))
    lis.append((float(ele1[1]),i))
print(lis)
lis.sort()
print(lis)
lis1=lis[1]
print(driver.find_element(By.XPATH,"//*[@id='stockTable']/tbody/tr["+str(lis1[1])+"]/td[2]").text)
time.sleep(10)