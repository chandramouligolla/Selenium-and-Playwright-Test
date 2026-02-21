import time
from datetime import datetime
from email.utils import format_datetime
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
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/selenium_practice_page.html")
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Simple Alert']").click()
time.sleep(1)
ele1=driver.switch_to.alert
print(ele1.text)
ele1.accept()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Confirmation Alert']").click()
ele2=driver.switch_to.alert
print(ele2.text)
ele2.accept()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Prompt Alert']").click()
ele3=driver.switch_to.alert
print(ele3.text)
ele3.send_keys("12345")
ele3.accept()
ele5=driver.find_element(By.XPATH,"//p[@id='alert-status']")
print(ele5.text)
