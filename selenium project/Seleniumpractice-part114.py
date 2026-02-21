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
ele=driver.find_element(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-input']")
ele.send_keys("cha")
ele.submit()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='wikipedia-search-results']//a[text()='ChatGPT']").click()
time.sleep(2)
lis=[]
window_ids=driver.window_handles
for window_id in window_ids:
    lis.append(window_id)
driver.switch_to.window(lis[1])
tit=driver.title
print(tit)
time.sleep(2)
driver.switch_to.window(lis[0])
tit1=driver.title
print(tit1)



