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
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
no_of_element=driver.find_elements(By.XPATH,"//table[@id='taskTable']//tbody/tr/td[4]")
no_of_rows=driver.find_elements(By.XPATH,"//table[@id='taskTable']//tbody/tr")
print("no of rows",len(no_of_rows))
no_of_columns=driver.find_elements(By.XPATH,"//table[@id='taskTable']//tbody/tr[1]/td")
print("no of columns",len(no_of_columns))
ele3=driver.find_element(By.XPATH,"//table[@id='taskTable']//tbody/tr[1]/td[1]")
no_of_units=driver.execute_script("arguments[0].scrollIntoView();",ele3)
time.sleep(5)
lis=[]
for i in range(1,len(no_of_rows)+1):
    ele=driver.find_element(By.XPATH,"//table[@id='taskTable']//tbody/tr["+str(i)+"]/td[5]")
    ele1=ele.text.strip().split(" ")
    lis.append((float(ele1[0]),i))
lis.sort()
print(lis)
time.sleep(5)
adj_element=driver.find_element(By.XPATH,"//table[@id='taskTable']//tbody/tr["+str(lis[0][1])+"]/td[4]")
print(adj_element.text)



