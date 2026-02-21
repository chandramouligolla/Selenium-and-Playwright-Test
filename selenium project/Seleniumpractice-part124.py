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
time.sleep(1)
print(driver.title)
driver.find_element(By.XPATH,"//button[text()='New Tab']").click()
time.sleep(1)
wind_id=driver.window_handles
lis=[]
for i in wind_id:
    lis.append(i)
driver.switch_to.window(lis[1])
print(driver.title)
time.sleep(1)
driver.switch_to.window(lis[0])
print(driver.title)
driver.find_element(By.XPATH,"//*[@id='PopUp']").click()
lis1=[]
wind_id1=driver.window_handles
for i in wind_id1:
    lis1.append(i)
driver.switch_to.window(lis1[1])
print(driver.title)
driver.switch_to.window(lis[0])
print(driver.title)



