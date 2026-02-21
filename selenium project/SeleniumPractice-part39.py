import time
from datetime import datetime
from email.utils import format_datetime
import requests
import os
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
preferences={"download.default_directory":os.getcwd()}
ops.add_experimental_option("prefs",preferences)
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/selenium_practice_page.html")
time.sleep(2)
filepath=r"C:\Users\DELL\Documents\practicepagelinks.txt"
driver.find_element(By.XPATH,"//*[@id='file-upload']").send_keys(filepath)
time.sleep(2)
ele=driver.find_element(By.XPATH,'//button[text()="Download Sample Text File"]')
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.find_element(By.XPATH,'//button[text()="Download Sample Text File"]').click()
time.sleep(5)