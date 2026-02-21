#dynamic button and alerts and popups

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
for i in range(3):
    driver.find_element(By.XPATH,"//button[@name='start' or @name='stop']").click()

#alert windows
driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
alert=driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()
driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
confirm=driver.switch_to.alert
print(confirm.text)
time.sleep(2)
alert.dismiss()
driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()
prompt=driver.switch_to.alert
print(prompt.text)
message="Happy Diwali"
prompt.send_keys(message)
alert.accept()
expected_result=driver.find_element(By.XPATH,"//p[@id='demo']").text
if expected_result.strip()==f"Hello {message}! How are you today?":
    print("woohoo woohoo its working")
else:
    print("Mismatch. Got:", expected_result)


