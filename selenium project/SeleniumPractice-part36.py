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
act=ActionChains(driver)
time.sleep(3)
act.move_to_element(driver.find_element(By.CSS_SELECTOR,".tooltip-trigger")).perform()
time.sleep(3)
act.double_click(driver.find_element(By.CSS_SELECTOR,"#double-click-box")).perform()
time.sleep(3)
act.drag_and_drop((driver.find_element(By.CSS_SELECTOR,"#draggable")),(driver.find_element(By.CSS_SELECTOR,"#droppable"))).perform()
time.sleep(3)