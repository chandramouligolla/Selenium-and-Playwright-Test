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
driver.get("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='New Window Message']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='New Window Message']").click()
wind_ids=driver.window_handles
lis1=[]
for wind_id in wind_ids:
    lis1.append(wind_id)
print(lis1)
driver.switch_to.window(lis1[1])
print(driver.title)
print(driver.find_element(By.XPATH,"/html/body/main/div/div").text)

