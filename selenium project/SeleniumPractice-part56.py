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
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
No_of_rows=driver.find_elements(By.XPATH,"//table[@id='productTable']/tbody/child::tr")
ele=driver.find_element(By.XPATH,"//table[@id='productTable']/thead")
driver.execute_script("arguments[0].scrollIntoView();",ele)
no_of_units_scrolled=driver.execute_script("return  window.pageYOffset;")
print("no of units scrolled",no_of_units_scrolled)
print("No of rows present",len(No_of_rows))
No_of_columns=driver.find_elements(By.XPATH,"//table[@id='productTable']/tbody/child::tr[1]/td")
print("No of columns present",len(No_of_columns))
No_of_pagn_present=driver.find_elements(By.XPATH,"//ul[@id='pagination']/child::li")
print("No of pagn present",len(No_of_pagn_present))
time.sleep(3)
for i in range(1,len(No_of_pagn_present)+1):
    for j in range(1,len(No_of_rows)+1):
        element=driver.find_element(By.XPATH,"//table[@id='productTable']/tbody/child::tr["+str(j)+"]")
        print(element.text)
    if (i+1)<=len(No_of_pagn_present):
        element1=driver.find_element(By.XPATH,"//ul[@id='pagination']/li["+str(i+1)+"]")
        element1.click()
print("all are  printed")
