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
sel_item=Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
sel_item.select_by_visible_text("Option2")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='alertbtn']").click()
ale=driver.switch_to.alert
print(ale.text)
ale.accept()
time.sleep(2)

