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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://letcode.in/droppable")
#time.sleep(2)
#driver.find_element(By.XPATH,"/html/body/app-root/app-test-site/section[2]/div/div/div/div[11]/app-menu/div/footer/a").click()
time.sleep(2)
source_element=driver.find_element(By.XPATH,"//*[@id='draggable']")
target_element=driver.find_element(By.XPATH,"//*[@id='droppable']")
act=ActionChains(driver)
act.drag_and_drop(source_element,target_element).perform()
time.sleep(3)

