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
driver.get("https://automationtesting.co.uk/hiddenElements.html")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".toggle").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Browser Tabs']").click()
time.sleep(2)
print("this is the title",driver.title)
print("this is the current url",driver.current_url)
driver.find_element(By.XPATH,"//input[@value='Open Tab']").click()
current=driver.current_window_handle
print("current window handle",current)
window_ids=driver.window_handles
lis=[]
for window_id in window_ids:
    lis.append(window_id)
driver.switch_to.window(lis[1])
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='APjFqb']").send_keys("instagram")
driver.save_screenshot(r"C:\Users\DELL\Downloads\screenshot.png")





