import requests
import time
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
driver.get("https://automationtesting.co.uk/actions.html")
time.sleep(2)
act=ActionChains(driver)
source_element=driver.find_element(By.XPATH,"//*[@id='dragtarget']")
target_element=driver.find_element(By.XPATH,"//*[@id='main']/div/div[1]/div[1]/div[2]")
act.drag_and_drop(source_element,target_element).perform()
time.sleep(3)
ele=driver.find_element(By.XPATH,"//*[@id='doubClickStartText']")
act.double_click(ele).perform()
time.sleep(3)
act.key_down(Keys.SHIFT).perform()
driver.find_element(By.XPATH,"//p[text()='Hold Shift & Click Here']").click()
ale=driver.switch_to.alert
print(ale.text)
ale.accept()
act.key_up(Keys.SHIFT).perform()
time.sleep(3)
ele3=driver.find_element(By.XPATH,"//*[@id='click-box']")
act.key_down(Keys.CONTROL).perform()
act.click_and_hold(ele3).perform()
time.sleep(3)
act.key_up(Keys.CONTROL).perform()
time.sleep(1)

