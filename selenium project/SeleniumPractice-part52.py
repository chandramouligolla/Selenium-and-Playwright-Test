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
driver.get("https://automationtesting.co.uk/index.html")
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,".toggle").click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[text()='Actions']").click()
time.sleep(2)
act=ActionChains(driver)
first_element=driver.find_element(By.XPATH,"//p[@id='dragtarget']")
second_element=driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div[1]/div[2]")
act.drag_and_drop(first_element,second_element).perform()
time.sleep(1)
act.key_down(Keys.SHIFT).perform()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[2]/div[2]/div/div/div/p").click()
#act.key_up(Keys.SHIFT).perform()
alert_window=driver.switch_to.alert
print(alert_window.text)
alert_window.accept()
act.key_up(Keys.SHIFT).perform()
time.sleep(3)
ele=driver.find_element(By.XPATH,"//*[@id='click-box']")
act.click_and_hold(ele).perform()
time.sleep(4)
act.release().perform()
time.sleep(2)


