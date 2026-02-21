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
val="2/3"
lis=[]
for i in val:
    lis.append(i)
print(lis)
operator1=int(lis[0])
operator2=lis[1]
operator3=int(lis[2])
print(operator1,operator2,operator3)
if operator2=="+":
    result=operator1+operator3
    print(result)
elif operator2=="-":
    result=operator1-operator3
    print(result)
elif operator2=="*":
    result=operator1*operator3
    print(result)
else:
    result=operator1/operator3
    print(result)

