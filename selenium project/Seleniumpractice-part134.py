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
driver.get("https://testautomationpractice.blogspot.com/#")
time.sleep(2)
lis=driver.find_elements(By.XPATH,"//div[@id='broken-links']//a")
for i in range(len(lis)):
    ele=lis[i].get_attribute("href")
    re=requests.head(ele)
    if re.status_code>=400:
        print("all are working fine")
    else:
        print("not working")
