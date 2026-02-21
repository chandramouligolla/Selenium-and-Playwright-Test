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
driver.get("https://testerbud.com/practice-different-ui-elements")
ele=driver.find_element(By.XPATH,"//label[text()='Virtual Scrolling (Simulated):']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(3)
ele1=driver.find_element(By.XPATH,"//div[text()='Item 17']")
driver.execute_script("arguments[0].scrollIntoView();",ele1)
ele1.click()
units=driver.execute_script("return window.pageYOffset;")
print(units)


