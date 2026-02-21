from os import fsdecode
import time
import requests
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
driver.get("https://testautomationpractice.blogspot.com/#")
time.sleep(1)
ele=driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']")
ele.send_keys("Insta")
ele.submit()
time.sleep(3)
curr=driver.current_window_handle
driver.switch_to.window(curr)
print(driver.title)
driver.find_element(By.XPATH,"//div[@id='wikipedia-search-result-link']/a[text()='Instagram']").click()
time.sleep(5)
wind_ids=driver.window_handles
lis=[]
for i in wind_ids:
    lis.append(i)
driver.switch_to.window(lis[1])
print(driver.title)
time.sleep(2)




