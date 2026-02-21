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
driver.get("https://www.tutorialspoint.com/selenium/practice/buttons.php")
time.sleep(1)
act=ActionChains(driver)
ele=driver.find_element(By.XPATH,"//button[text()='Click Me']")
ele2=driver.find_element(By.XPATH,"//button[text()='Right Click Me']")
ele3=driver.find_element(By.XPATH,"//button[text()='Double Click Me']")
act.move_to_element(ele).click().perform()
time.sleep(1)
act.context_click(ele2).perform()
act.double_click(ele3).perform()
time.sleep(3)



