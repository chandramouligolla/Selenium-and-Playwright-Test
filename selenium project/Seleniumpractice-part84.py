import time
from datetime import datetime
from email.utils import format_datetime
from os import fsdecode
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
#ops.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://www.tutorialspoint.com/selenium/practice/scroll-top.php")
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(2)
no_of_units=driver.execute_script("return window.pageYOffset;")
time.sleep(2)
print(no_of_units)
time.sleep(2)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(2)
no_of_units1=driver.execute_script("return window.pageYOffset;")
print(no_of_units1)
