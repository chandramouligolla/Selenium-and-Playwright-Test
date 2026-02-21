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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(1)
print(driver.find_element(By.XPATH,"//input[@id='displayed-text']").is_displayed())
driver.find_element(By.XPATH,"//input[@id='hide-textbox']").click()
print(driver.find_element(By.XPATH,"//input[@id='displayed-text']").is_displayed())
No_of_rows=driver.find_elements(By.XPATH,"//div[@class='tableFixHead']//tbody/tr/td[4]")
print(len(No_of_rows))
No_of_columns=driver.find_elements(By.XPATH,"//div[@class='tableFixHead']//thead/tr/th")
print(len(No_of_columns))
lis=[]
for i in range(1,len(No_of_rows)+1):
    ele=driver.find_element(By.XPATH, "//div[@class='tableFixHead']//tbody/tr["+str(i)+"]/td[4]").text
    lis.append(int(ele))
print(lis)
print(max(lis))
print(min(lis))
count=0
for cou in range(len(lis)):
    count=count+lis[cou]
print(count)
