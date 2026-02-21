
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
list_of_ele=driver.find_elements(By.XPATH,"//div[@id='form-elements']/div[1]/input")
for i in list_of_ele:
    if i.get_attribute('value')=="car":
        i.click()
        time.sleep(3)
        break
time.sleep(2)
for i in list_of_ele:
    if not(i.is_selected()):
        time.sleep(2)
        i.click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Deselect All']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='male']").click()
time.sleep(2)
ele1=Select(driver.find_element(By.XPATH,"//select[@id='cars']"))
all_options=ele1.options
for i in all_options:
    print(i.text)
ele1.select_by_visible_text("Mercedes")
time.sleep(2)





