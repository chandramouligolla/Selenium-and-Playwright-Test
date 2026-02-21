import time
from datetime import datetime
from email.utils import format_datetime
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://artoftesting.com/samplesiteforselenium")
act=ActionChains(driver)
ele1=driver.find_element(By.XPATH,"//button[@id='dblClkBtn']")
time.sleep(3)
act.move_to_element(ele1).double_click(ele1).perform()
time.sleep(3)
alert_popup=driver.switch_to.alert
print(alert_popup.text)
alert_popup.accept()
########## Radio Buttons ##################
ele2=driver.find_element(By.XPATH,"//input[@id='male']")
print(ele2.is_selected())
ele3=driver.find_element(By.XPATH,"//input[@id='female']")
print(ele3.is_selected())
print("after clicking on male radio button")
ele2=driver.find_element(By.XPATH,"//input[@id='male']")
ele2.click()
print(ele2.is_selected())
ele3=driver.find_element(By.XPATH,"//input[@id='female']")
print(ele3.is_selected())
print("after clicking on female radio button")
time.sleep(1)
ele3=driver.find_element(By.XPATH,"//input[@id='female']")
time.sleep(1)
ele3.click()
print(ele3.is_selected())
ele2=driver.find_element(By.XPATH,"//input[@id='male']")
print(ele2.is_selected())
####checkboes#######
ele4=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for i in ele4:
    print(i.get_attribute('value'))
    print(i.text)
    if not(i.is_selected()):
        i.click()











