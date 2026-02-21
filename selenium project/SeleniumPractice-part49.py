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
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/Captcha.html")
time.sleep(2)
text_to_validate=driver.find_element(By.XPATH,"//div[@id='math-captcha']").text
print("this is the string which is to validate",text_to_validate)
lis=text_to_validate.split("=")
lis1=lis[0].split(" ")
listy_to_validate1=lis1
print(listy_to_validate1)
print(type(listy_to_validate1))
num1=int(listy_to_validate1[0])
operator=(listy_to_validate1[1])
num2=int(listy_to_validate1[2])
print(num1,operator,num2)
dicti={'+':"add",'-':"sub",'*':"mul",'/':"div"}
num=0
if operator in dicti.keys():
    operator_value=dicti[operator]
    if operator_value=="add":
        num=str(num1+num2)
    if operator_value=="sub":
        num=str(num1-num2)
    if operator_value=="mul":
        num=str(num1*num2)
    if operator_value=="div":
        num=str(num1/num2)
else:
    print(operator)
print(num)
print(type(num))
driver.find_element(By.XPATH,"//input[@id='math-captcha-input']").send_keys(num)
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/button").click()
time.sleep(10)





