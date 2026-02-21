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
driver.get("https://www.tutorialspoint.com/selenium/practice/frames.php")
time.sleep(1)
ele1=[]
ele_s=driver.find_elements(By.XPATH,"//iframe[@src='new-tab-sample.php']")
for ele in ele_s:
    ele1.append(ele)
print(ele1)
driver.switch_to.frame(ele1[0])
driver.find_element(By.XPATH,"/html/body/div/header/div[3]/a").click()
print(driver.title)
# wind_id=driver.window_handles
# lis=[]
# for i in wind_id:
#     lis.append(i)
# time.sleep(5)
driver.switch_to.default_content()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='headingThree']/button").click()
time.sleep(3)
driver.switch_to.frame(ele1[1])
time.sleep(3)
element=driver.find_element(By.XPATH,"/html/body/main/div/div").text
print(element)
time.sleep(3)
