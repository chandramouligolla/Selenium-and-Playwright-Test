#text boxes

import time
from datetime import datetime
from email.utils import format_datetime

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.XPATH,"//*[@id='input1']"))
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='input1']").send_keys("chandra")
driver.find_element(By.XPATH,"//*[@id='btn1']")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='input2']").send_keys("Mouli")
driver.find_element(By.XPATH,"//*[@id='btn2']")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='input3']").send_keys("Golla")
driver.find_element(By.XPATH,"//*[@id='btn3']")
time.sleep(2)