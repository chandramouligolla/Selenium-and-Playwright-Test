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
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='key-press-input']").click()
act=ActionChains(driver)
act.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)
ele2=driver.find_element(By.CSS_SELECTOR,"#key-press-result")
print(ele2.text)
if ele2.text.__contains__("ArrowDown"):
    print("arrow down clicked")
else:
    print("nothing clicked")
act.send_keys(Keys.ALT).perform()
time.sleep(2)
ele2=driver.find_element(By.CSS_SELECTOR,"#key-press-result")
print(ele2.text)
if ele2.text.__contains__("Alt"):
    print("alt clicked")
else:
    print("nothing clicked")
act.send_keys(Keys.SHIFT).perform()
time.sleep(2)
ele2=driver.find_element(By.CSS_SELECTOR,"#key-press-result")
print(ele2.text)
if ele2.text.__contains__("Shift"):
    print("Shift clicked")
else:
    print("nothing clicked")
act.send_keys(Keys.CONTROL).perform()
time.sleep(2)
ele2=driver.find_element(By.CSS_SELECTOR,"#key-press-result")
print(ele2.text)
if ele2.text.__contains__("Control"):
    print("Control clicked")
else:
    print("nothing clicked")
act.send_keys(Keys.TAB).perform()
time.sleep(2)
ele2=driver.find_element(By.CSS_SELECTOR,"#key-press-result")
print(ele2.text)
if ele2.text.__contains__("Tab"):
    print("Tab clicked")
else:
    print("nothing clicked")

