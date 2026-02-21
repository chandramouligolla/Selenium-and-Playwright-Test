#iframes part2

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
driver.get("https://automationtesting.co.uk")
print(driver.title)
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/a").click()
time.sleep(5)
ele=driver.find_element(By.XPATH,"//a[text()='iFrames']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(5)
no_of_values_moved=driver.execute_script("return window.pageYOffset;")
print(no_of_values_moved)
