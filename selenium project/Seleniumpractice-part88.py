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
#ops.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationcentral.com/demo/dropdown.html")
time.sleep(2)
# select_ele=Select(driver.find_element(By.XPATH,"//*[@id='simple-dropdown']/select"))
# select_ele.select_by_visible_text("Option 2")
# all_options=select_ele.options
# for i in all_options:
#     print(i.text)
# driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/button[2]").click()
# time.sleep(1)
# select_ele=Select(driver.find_element(By.XPATH,"//*[@id='styled-dropdown']/select"))
# select_ele.select_by_visible_text("Styled Option 2")
# all_options=select_ele.options
# for i in all_options:
#     print(i.text)

# driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/button[3]").click()
# time.sleep(1)
# select_ele=Select(driver.find_element(By.XPATH,"//*[@id='multi-select-dropdown']/select"))
# act=ActionChains(driver)
# act.key_down(Keys.CONTROL).perform()
# select_ele.select_by_visible_text("Option 2")
# select_ele.select_by_visible_text("Option 5")
# time.sleep(1)
# act.key_up(Keys.CONTROL).perform()
# all_options=select_ele.options
# for i in all_options:
#     print(i.text)
driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/button[4]").click()
select_ele=Select(driver.find_element(By.XPATH,"//*[@id='grouped-dropdown']/select"))
select_ele.select_by_visible_text("Option 3")
time.sleep(4)

