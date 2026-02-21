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
act=ActionChains(driver)
ele=driver.find_element(By.XPATH,"//button[text()='Point Me']")
ele1=driver.find_element(By.XPATH,"//div[@class='dropdown-content']/a[2]")
act.move_to_element(ele).perform()
time.sleep(1)
act.move_to_element(ele1).click().perform()
time.sleep(2)

