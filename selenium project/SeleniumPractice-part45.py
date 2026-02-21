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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/Sliders.html")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='startDate']").send_keys("24-05-2005")
time.sleep(4)
driver.find_element(By.XPATH,"//button[text()='Show Confirm Dialog']").click()
time.sleep(2)
ele3=driver.switch_to.alert
ele3.accept()
time.sleep(2)
ele3.accept()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='Tab2']").click()
time.sleep(2)

