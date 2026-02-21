from os import fsdecode
import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os
location=os.getcwd()
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
ops.add_argument("--disabled-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/#")
time.sleep(1)
# act=ActionChains(driver)
# ele=driver.find_element(By.XPATH,"//*[@id='field1']")
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# ele.click()
# time.sleep(2)
# act.key_down(Keys.CONTROL).send_keys("a").perform()
# time.sleep(2)
# act.key_down(Keys.CONTROL).send_keys("c").perform()
# act.key_up(Keys.CONTROL).perform()
# act.send_keys(Keys.TAB).perform()
# time.sleep(2)
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# time.sleep(2)
act=ActionChains(driver)
ele=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
act.double_click(ele).perform()
time.sleep(3)
driver.execute_script("arguments[0].scrollIntoView();",ele)
source_ele=driver.find_element(By.XPATH,"//*[@id='draggable']")
target_ele=driver.find_element(By.XPATH,"//*[@id='droppable']")
act.drag_and_drop(source_ele,target_ele).perform()
time.sleep(3)






