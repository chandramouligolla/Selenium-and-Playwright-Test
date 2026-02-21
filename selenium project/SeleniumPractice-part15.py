#links

import time
from datetime import datetime
from email.utils import format_datetime

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
all_broken_links=driver.find_elements(By.XPATH,"//*[@id='broken-links']/a")
count=0
for all_broken_link in all_broken_links:
    url=all_broken_link.get_attribute("href")
    res=requests.head(url)
    if res.status_code>=400:
        count+=1
        print(url,"it is a broken link")
print(count)

