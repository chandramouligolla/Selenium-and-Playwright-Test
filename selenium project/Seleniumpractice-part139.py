import requests
import time
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
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='autocomplete']").send_keys("ind")
time.sleep(2)
driver.find_element(By.XPATH,"//li[@class='ui-menu-item']/div[text()='India']").click()
time.sleep(2)


