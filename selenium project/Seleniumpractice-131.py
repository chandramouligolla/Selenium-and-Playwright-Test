from os import fsdecode
import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os
location=os.getcwd()
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
ops.add_argument("--disabled-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/#")
time.sleep(2)
ele=driver.find_element(By.XPATH,"//tr[@id='headers']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
No_of_rows=driver.find_elements(By.XPATH,"//tbody[@id='rows']/tr")
print(len(No_of_rows))
NO_of_columns=driver.find_elements(By.XPATH,"//tr[@id='headers']/th")
print(len(NO_of_columns))
lis=[]
for i in range(1,len(No_of_rows)+1):
    ele=driver.find_element(By.XPATH,"//tbody[@id='rows']/tr["+str(i)+"]/td[4]")
    print(ele.text)
    lis.append((ele.text,i))
print(lis)
lis.sort()
print(lis)
ele1=driver.find_element(By.XPATH,"//tbody[@id='rows']/tr["+str(lis[0][1])+"]/td[3]")
print(ele1.text)
time.sleep(1)

