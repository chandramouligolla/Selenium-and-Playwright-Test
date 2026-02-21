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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/Captcha.html")
time.sleep(2)
text_capture=driver.find_element(By.XPATH,"//div[@id='text-captcha']").text
print("this is the captcha",text_capture)
driver.find_element(By.XPATH,"//input[@id='text-captcha-input']").send_keys(text_capture)
driver.find_element(By.XPATH,"//button[text()='Validate']").click()
time.sleep(5)