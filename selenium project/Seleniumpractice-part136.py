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
driver.get("https://automationtesting.co.uk/predictive.html")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='myInput']").send_keys("r")
time.sleep(3)
ele=driver.find_elements(By.XPATH,"//div[@id='myInputautocomplete-list']/div")
for i in range(len(ele)):
    print(ele[i].text)
    if ele[i].text=="Russia":
        ele[i].click()
        time.sleep(3)
        break

# dropdown_container = driver.find_element(By.XPATH, "//div[@id='myInputautocomplete-list']")
#
# options = dropdown_container.find_elements(By.XPATH, "./div")
#
# for option in options:
#     try:
#         text = option.text
#         print(text)
#         if "Russia" in text:
#             option.click()
#             time.sleep(2)
#             break
#     except Exception as e:
#         print(f"Error: {e}")



