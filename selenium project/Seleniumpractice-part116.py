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
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("chandra")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("chandra.gmail.com")
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("8008505587")
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("2-33/2 rangarajupeta")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='male']").click()
time.sleep(1)
