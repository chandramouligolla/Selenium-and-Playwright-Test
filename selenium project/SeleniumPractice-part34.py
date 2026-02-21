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
ele=driver.find_element(By.XPATH,"//iframe[@id='sample-iframe']")
driver.switch_to.frame(ele)
driver.find_element(By.XPATH,"//button[text()='Click Me (Inside Frame)']").click()
time.sleep(2)
driver.switch_to.alert.accept()
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//button[text()='Open New Window']").click()
time.sleep(2)