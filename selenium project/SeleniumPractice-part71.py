#
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
driver.get("https://www.tutorialspoint.com/selenium/practice/radio-button.php")
time.sleep(1)
rad1=driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[1]/input")
print(rad1.is_enabled())
rad1.click()
rad2=driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[3]/input")
print(rad2.is_enabled())
rad2.click()
rad3=driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[5]/input")
print(rad3.is_enabled())



