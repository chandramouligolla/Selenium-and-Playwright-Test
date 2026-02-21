#scroll

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
#element=driver.find_element(By.XPATH,"//*[@id='HTML1']/h2")
# tab_element=driver.execute_script("arguments[0].scrollIntoView();",element)
# time.sleep(2)
# tab_element_dist=driver.execute_script("return window.pageYOffset;")
# print("the table element",tab_element_dist)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# down_element=driver.execute_script("return window.pageYOffset;")
# print(down_element)
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
# down_element=driver.execute_script("return window.pageYOffset;")
# print(down_element)
driver.execute_script("window.scrollBy(0,3000)","")
time.sleep(2)
down_element=driver.execute_script("return window.pageYOffset;")
print(down_element)
