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
driver.get("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/button[1]").click()
time.sleep(2)
wind_id=driver.window_handles
lis=[]
for wind_i in wind_id:
    lis.append(wind_i)
print(lis)
driver.switch_to.window(lis[0])
print("The title of parent page is",driver.title)
driver.switch_to.window(lis[1])
print("The title of child page is",driver.title)
time.sleep(2)
driver.switch_to.window(lis[0])
driver.find_element(By.XPATH,"//button[text()='New Window']").click()
wind_id1=driver.window_handles
lis1=[]
for wind_i1 in wind_id1:
    lis1.append(wind_i1)
print(lis1)
driver.switch_to.window(lis1[0])
print("The title of parent page is",driver.title)
driver.switch_to.window(lis1[1])
print("The title of child page is",driver.title)
time.sleep(2)
