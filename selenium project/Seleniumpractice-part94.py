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
driver.get("https://testautomationcentral.com/demo/dynamic_loading.html")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@onclick='startLoading()']").click()
time.sleep(2)
my_wait=WebDriverWait(driver,10)
my_wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='loading-content']/p")))
message=driver.find_element(By.XPATH,"//div[@id='loading-content']/p").text
print(message)
