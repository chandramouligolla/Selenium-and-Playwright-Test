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
driver.get("https://testautomationpractice.blogspot.com/#")
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Simple Alert']").click()
ale=driver.switch_to.alert
print(ale.text)
ale.accept()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Confirmation Alert']").click()
ale1=driver.switch_to.alert
print(ale1.text)
ale1.accept()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Prompt Alert']").click()
ale3=driver.switch_to.alert
ale3.send_keys("mouli")
print(ale3.text)
time.sleep(5)
ale3.accept()
ele3=driver.find_element(By.XPATH,"//*[@id='demo']")
print(ele3.text)
time.sleep(1)
