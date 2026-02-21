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
act=ActionChains(driver)
time.sleep(1)
first_drop=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
print(first_drop.location)
second_drop=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
print(second_drop.location)
act.drag_and_drop_by_offset(first_drop,100,0).perform()
act.drag_and_drop_by_offset(second_drop,100,0).perform()
print(first_drop.location)
print(second_drop.location)
time.sleep(10)

