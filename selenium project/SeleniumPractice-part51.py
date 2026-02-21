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
driver.get("https://automationtesting.co.uk/calculator.html")
time.sleep(2)
val="3*9"
num1=""
num2=""
operator=""
for i in val:
    if num1=="":
        num1=str(i)
    elif num1!="" and operator=="":
        operator=str(i)
    else:
        num2=str(i)
print(num1,num2,operator)
all_elements=driver.find_elements(By.XPATH,"//*[@id='main']/div/div/div/table/tbody/tr/td/input")
for element in all_elements:
    if element.get_attribute('value')==num1:
        element.click()
        break
for element in all_elements:
    if element.get_attribute('value')==operator:
        element.click()
        break
for element in all_elements:
    if element.get_attribute('value')==num2:
        element.click()
        break

driver.find_element(By.XPATH,"//*[@id='main']/div/div/div/table/tbody/tr[5]/td[3]/input").click()
time.sleep(10)
result=driver.find_element(By.XPATH,"//input[@id='result']").text
print(result,"the type",type(result))
if result==27:
    print("The result is perfect")



# ELEMENT=driver.find_element(By.XPATH,"//*[@id='main']/div/div/div/table/tbody/tr[3]/td[1]/input")
# print(ELEMENT.get_attribute("value"))

