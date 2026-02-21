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
ops.add_argument("--disabled-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://practice.expandtesting.com/otp-login")
time.sleep(1)
otp=driver.find_element(By.XPATH,"//*[@id='core']/div/div/div[1]/div/ul/li[2]").text
print(otp)
otp_number_list=otp.strip().split(":")
print(otp_number_list)
striped_number=otp_number_list[1].strip()
print(striped_number)



