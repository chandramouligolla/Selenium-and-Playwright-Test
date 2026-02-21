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
ele=Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
all_options=ele.options
for option in all_options:
    print(option.text)
act=ActionChains(driver)
act.key_down(Keys.CONTROL)
driver.find_element(By.XPATH,"//option[text()='Red']").click()
driver.find_element(By.XPATH,"//option[text()='Blue']").click()
act.key_up(Keys.CONTROL)
driver.find_element(By.XPATH,"//textarea[@id='message']").send_keys("1322344324fdgbvfdgfdgg")
time.sleep(5)