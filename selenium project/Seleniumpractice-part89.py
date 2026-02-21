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
driver.get("https://testautomationcentral.com/demo/textboxes.html")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='simple-textbox']/input").send_keys("acha")
driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/button[2]").click()
driver.find_element(By.XPATH,"//*[@id='placeholder-textbox']/input").send_keys("tichey")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/button[5]").click()
ele=driver.find_element(By.XPATH,"//*[@id='readonly-textbox']/input").get_attribute('value')
print(ele)
driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/button[6]").click()
ele1=driver.find_element(By.XPATH,"//*[@id='disabled-textbox']/input")
print(ele1.is_enabled())
time.sleep(2)




