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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://letcode.in/window")
driver.find_element(By.XPATH,"//button[text()='Open Home Page']").click()
time.sleep(2)
window_ids=driver.window_handles
lis=[]
for window_id in window_ids:
    driver.switch_to.window(window_id)
    print(driver.title)
    lis.append(window_id)
time.sleep(2)
driver.switch_to.window(lis[0])
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Muiltiple windows']").click()
time.sleep(1)


