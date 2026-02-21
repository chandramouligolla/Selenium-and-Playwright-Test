#input text boxes
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
driver.get("https://www.qaplayground.com/practice")
driver.find_element(By.XPATH,"//span[text()='Edit']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='movieName']").send_keys("original gangstar")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='appendText']").send_keys(". How are you?")
time.sleep(2)
act=ActionChains(driver)
act.key_down(Keys.TAB).perform()
time.sleep(2)
ele1=driver.find_element(By.XPATH,"//input[@id='insideText']")
time.sleep(2)
expected_text="QA PlayGround"
if expected_text==ele1.get_attribute('value'):
    print("its equal")
else:
    print("not equal")
driver.find_element(By.XPATH,"//input[@id='clearText']").clear()
time.sleep(2)
ele2=driver.find_element(By.XPATH,"//input[@id='disabledInput']")
time.sleep(2)
print("the enable status",ele2.is_enabled())
time.sleep(2)


