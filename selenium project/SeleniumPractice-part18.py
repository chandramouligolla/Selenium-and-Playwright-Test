#hidden elements

import time
from datetime import datetime
from email.utils import format_datetime


import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
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
print(driver.title)
driver.find_element(By.XPATH,"//*[@id='PageList1']/div/ul/li[2]/a").click()
time.sleep(5)
# ele=driver.find_element(By.XPATH,"//*[@id='Blog1']/div[1]/div/div/div/div/div[2]/div[1]/input[1]")
# time.sleep(2)
# ele.send_keys("chhh")
ele=driver.find_element(By.XPATH,"//*[@id='container']/input[2]")
print(ele.is_displayed())
print("after clicking on the button for input box")
driver.find_element(By.XPATH,"//button[text()='Toggle Input Box 2']").click()
time.sleep(3)
ele=driver.find_element(By.XPATH,"//*[@id='container']/input[2]")
time.sleep(2)
print(ele.is_displayed())
ele.send_keys("chhh")

ele2=driver.find_element(By.XPATH,"//*[@id='checkbox2']")
print(ele2.is_displayed())


