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
time.sleep(2)
element=driver.find_element(By.XPATH,"//li[@id='menu-item-97']")
act=ActionChains(driver)
act.move_to_element(element).perform()
time.sleep(3)
element1=driver.find_element(By.XPATH,"//li[@id='menu-item-97']//ul/li[3]")
# act.move_to_element(element1).perform()
element1.click()
