import time
import os
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
preferences={"download.default_directory":os.getcwd()}
ops.add_experimental_option("prefs",preferences)
#ops.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://www.tutorialspoint.com/selenium/practice/upload-download.php")
time.sleep(1)
driver.find_element(By.XPATH,"//a[text()='Download']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='uploadFile']").send_keys(r"C:\Users\DELL\Downloads\info.txt")
time.sleep(2)

