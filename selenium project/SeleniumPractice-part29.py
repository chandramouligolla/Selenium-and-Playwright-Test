#custome page

import time
from datetime import datetime
from email.utils import format_datetime
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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/selenium_practice_page.html")
#driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/New_practice.html")
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("chandra")
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='Clear Field']").click()
driver.find_element(By.XPATH,"//button[@id='simple-button']").click()
ele1=driver.switch_to.alert
print(ele1.text)
ele1.accept()
driver.find_element(By.XPATH,"//*[@value='Input Button (by Value)']").click()
ele2=driver.switch_to.alert
print(ele2.text)
ele2.accept()
driver.find_element(By.LINK_TEXT,"This is a sample link (by LinkText)").click()
ele3=driver.switch_to.alert
print(ele3.text)
ele3.accept()
driver.find_element(By.PARTIAL_LINK_TEXT,"(by PartialLinkText)").click()
ele4=driver.switch_to.alert
print(ele4.text)
ele4.accept()
time.sleep(3)
#ele5=driver.find_element(By.XPATH,"//div[@id='text-display']/span").text
ele5=driver.find_element(By.XPATH,"//div[@id='text-display']").text
print(ele5)
