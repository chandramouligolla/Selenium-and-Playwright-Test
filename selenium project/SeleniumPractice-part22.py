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
my_wait=WebDriverWait(driver,10)
# driver.find_element(By.XPATH,"//a[text()='This is a link']")
ele1=my_wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='This is a link']")))
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView();",ele1)
No_of_units=driver.execute_script("return window.pageYOffset;")
time.sleep(2)
print("no of units moved",No_of_units)
ele1.click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='fname']").send_keys("chandra")
driver.find_element(By.XPATH,"//button[@id='idOfButton']").click()

