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
driver.get("https://testautomationpractice.blogspot.com/#")
no_of_rows=driver.find_elements(By.XPATH,"//table[@id='productTable']//tbody/tr")
print(len(no_of_rows))
no_of_columns=driver.find_elements(By.XPATH,"//table[@id='productTable']/thead/tr/th")
print(len(no_of_columns))
no_of_pag=driver.find_elements(By.XPATH,"//ul[@id='pagination']/li")
print(len(no_of_pag))
for i in range(1,len(no_of_pag)+1):
    for j in range(1,len(no_of_rows)+1):
        ele=driver.find_element(By.XPATH,"//table[@id='productTable']//tbody/tr["+str(j)+"]")
        print(ele.text)
    if i+1 != len(no_of_pag)+1:
        driver.find_element(By.XPATH,"//ul[@id='pagination']//li["+str(i+1)+"]").click()

        


