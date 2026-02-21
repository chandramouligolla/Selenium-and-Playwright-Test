import requests
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os
location=os.getcwd()
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
ops.add_argument("--disabled-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/Captcha.html")
time.sleep(2)
ele=driver.find_element(By.XPATH,"//*[@id='math-captcha']").text
print(ele)
ele1=ele.strip().split("=")
print(ele1)
ele2=ele1[0].strip().split(' ')
print(ele2)
first_element=int(ele2[0])
second_element=int(ele2[2])
operator=ele2[1]
if operator=="+":
    print(first_element+second_element)
elif operator=="-":
    print(first_element-second_element)
elif operator=="*":
    print(first_element*second_element)
elif operator=="/":
    print(first_element/second_element)
else:
    print(operator)