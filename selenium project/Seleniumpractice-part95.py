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
driver.get("https://testautomationcentral.com/demo/file_upload.html")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='file-input']").send_keys(r"C:\Users\DELL\Downloads\info.txt")
driver.find_element(By.XPATH,"//button[@class='bg-blue-500 text-white px-4 py-2 rounded']").click()
time.sleep(3)
