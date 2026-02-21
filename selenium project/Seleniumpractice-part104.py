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
driver.get("https://letcode.in/advancedtable")
No_of_rows=driver.find_elements(By.XPATH,"//table[@id='advancedtable']/tbody/tr")
print(len(No_of_rows))
time.sleep(2)
no_of_pagnitions=10
for i in range(1,no_of_pagnitions):
    for j in range(1,len(No_of_rows)+1):
        element=driver.find_element(By.XPATH,"//table[@id='advancedtable']//tbody/tr["+str(j)+"]")
        print(element.text)
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id='advancedtable_wrapper']/div[3]/div[2]/div/nav/button[4]").click()
    time.sleep(4)
time.sleep(5)




