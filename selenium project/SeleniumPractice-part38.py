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
driver.find_element(By.XPATH,"//*[@id='shortcut-input']").send_keys("chandra")
time.sleep(2)
act=ActionChains(driver)
act.send_keys(Keys.TAB).perform()
driver.find_element(By.XPATH,"//*[@id='keyboard-actions']/div[2]/button").click()
time.sleep(2)
ele=driver.find_element(By.XPATH,"//*[@id='copy-source']")
ele.click()
act.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(3)