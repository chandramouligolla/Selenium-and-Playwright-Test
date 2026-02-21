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
No_of_columns=driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th")
print(len(No_of_columns))
No_of_rows=driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr")
print(len(No_of_rows))
for i in range(2,len(No_of_rows)+1):
    ele=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td[3]")
    if ele.text=="Javascript":
        ele1=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td[2]")
        print(ele.text,"",ele1.text)


