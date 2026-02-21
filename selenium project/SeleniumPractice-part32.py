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
driver.find_element(By.XPATH,"//button[text()='Click to load text after 5 seconds']").click()
my_wait=WebDriverWait(driver,10)
ele=my_wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='delayed-text']")))
print(ele.text)
time.sleep(3)
ele2=driver.find_element(By.XPATH,"//*[@id='initially-disabled']")
print(ele2.is_enabled())
driver.find_element(By.XPATH,"//*[@id='enable-input-btn']").click()
my_wait=WebDriverWait(driver,10)
ele3=my_wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='initially-disabled']")))
ele3.send_keys("asddffg")
time.sleep(5)
ele3=driver.find_element(By.XPATH,"//*[@id='initially-disabled']")
ele3.send_keys("auehfd")
driver.find_element(By.XPATH,"//button[text()='Load Dynamic Table (3 seconds)']").click()
my_wait=WebDriverWait(driver,10)
ele4=my_wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="dynamic-table-container"]//tbody/tr')))
print(ele4.text)