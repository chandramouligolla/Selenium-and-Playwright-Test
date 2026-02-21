import time
from datetime import datetime
from email.utils import format_datetime
from os import fsdecode
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
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/Sliders.html")
time.sleep(2)
drop_down=Select(driver.find_element(By.XPATH,"//select[@id='fruitsSelect']"))
act=ActionChains(driver)
act.key_down(Keys.CONTROL)
drop_down.select_by_visible_text("Orange")
drop_down.select_by_visible_text("Strawberry")
act.key_up(Keys.CONTROL)
time.sleep(4)
ele=driver.find_element(By.XPATH,"//select[@id='fruitsSelect']/option[5]")
down_by=driver.execute_script("arguments[0].scrollIntoView();",ele)
print(driver.execute_script("return window.pageYOffset;"))
time.sleep(5)
driver.execute_script("window.scrollBy(0,409)","")
print(driver.execute_script("return window.pageYOffset;"))
time.sleep(3)