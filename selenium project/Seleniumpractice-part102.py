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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://letcode.in/table")
No_of_rows=driver.find_elements(By.XPATH,"//table[@id='shopping']//tbody/tr/td[2]")
print(len(No_of_rows))
count=[]
for i in No_of_rows:
    count.append(int(i.text))
print(count)
addition=(sum(count))
assert addition==858 , "not perfect"




