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
# ele=driver.find_element(By.XPATH,"//button[text()='START']")
# print(ele.is_displayed())
# ele.click()
# ele=driver.find_element(By.XPATH,"//button[text()='STOP']")
# print(ele.is_displayed())
for i in range(4):
    #driver.find_element(By.XPATH,"//button[contains(text(),'ST')]").click()
    driver.find_element(By.XPATH, "//button[starts-with(text(),'ST')]").click()
    time.sleep(1)

