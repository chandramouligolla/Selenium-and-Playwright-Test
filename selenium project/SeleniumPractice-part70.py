#text boxes

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
driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='fullname']").send_keys("Hi man")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Chgandramouli@gmail.com")
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("2-33/1")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("123456")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)


