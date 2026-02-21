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
driver.get("https://testautomationcentral.com/demo/alerts.html")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='alert-tab']/button").click()
ale=driver.switch_to.alert
print(ale.text)
ale.accept()
driver.find_element(By.XPATH,"//button[text()='Prompt']").click()
driver.find_element(By.XPATH,"//button[@class='bg-green-500 text-white px-4 py-2 rounded']").click()
ale1=driver.switch_to.alert
ale1.send_keys("Hi All")
time.sleep(3)
ale1.accept()
time.sleep(3)
message=driver.find_element(By.XPATH,"//p[@id='prompt-message']").text
lis=message.strip().split(":")
print(lis)
assert lis[1].strip()=='Hi All' ,"this not perfect"




