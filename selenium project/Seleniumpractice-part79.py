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
driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/div[1]/button").click()
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Click Me']").click()
time.sleep(6)
ele1=driver.switch_to.alert
print(ele1.text)
ele1.accept()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Click Me' and @onclick='myDesk()']").click()
time.sleep(2)
driver.switch_to.alert.accept()
driver.find_element(By.XPATH,"//button[text()='Click Me' and @onclick='myPromp()']").click()
ele2=driver.switch_to.alert
ele2.send_keys("12336655")
ele2.accept()
time.sleep(2)

