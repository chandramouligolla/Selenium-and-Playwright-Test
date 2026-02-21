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
driver.find_element(By.XPATH,"//button[text()='Open New Window']").click()
time.sleep(1)
winids=driver.window_handles
for wid in winids:
    print(wid)
driver.switch_to.window(winids[1])
ele1=driver.find_element(By.XPATH,"//button[text()='Open Two Windows']")
act=ActionChains(driver)
act.double_click(ele1).perform()
winids2=driver.window_handles
print(len(winids2))
for wid2 in winids2:
    print(wid2)
    driver.switch_to.window(wid2)
    print(driver.title)
    if driver.title=='Google':
        ele3=driver.find_element(By.XPATH,"//*[@id='APjFqb']")
        ele3.send_keys("deepseek ai")
        ele3.submit()
        time.sleep(4)
        print("last page title",driver.title)


