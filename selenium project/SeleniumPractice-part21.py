#working with download default directory for chrome

import time
from datetime import datetime
from email.utils import format_datetime
import requests
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
location="C:\\Users\\DELL\\Downloads"
ops.add_argument("--start-maximized")
preferences={"download.default_directory":location}
ops.add_experimental_option("prefs",preferences)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
driver.find_element(By.XPATH,"//a[text()='Download Files']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='inputText']").send_keys("chandra")
driver.find_element(By.XPATH,"//button[@id='generateTxt']").click()
my_wait=WebDriverWait(driver,10)
ele=my_wait.until(EC.presence_of_element_located((By.XPATH,"//a[@id='txtDownloadLink']")))
ele.click()
time.sleep(10)

