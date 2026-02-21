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
all_check_boxes=driver.find_elements(By.XPATH,"//*[@id='post-body-1307673142697428135']/div[4]/div")
# for i in all_check_boxes:
#     i.find_element(By.XPATH,"./descendant::label").click()
# time.sleep(4)
for i in all_check_boxes:
    ele=i.find_element(By.XPATH,"./descendant::label")
    if ele.text=="Friday":
        ele.click()
time.sleep(5)

