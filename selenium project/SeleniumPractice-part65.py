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
driver.get("https://testautomationpractice.blogspot.com/#")
time.sleep(3)
ele=driver.find_element(By.XPATH,"//h2[text()='Dynamic Web Table']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
print(driver.execute_script("return window.pageYOffset;"))
time.sleep(5)
No_of_rows=driver.find_elements(By.XPATH,"//tbody[@id='rows']/tr")
print(len(No_of_rows))
No_Of_columns=driver.find_elements(By.XPATH,"//table[@id='taskTable']/thead//th")
lis=[]
print(len(No_Of_columns))
for i in range(1,len(No_of_rows)+1):
    element=driver.find_element(By.XPATH,"//tbody[@id='rows']/tr["+str(i)+"]/td[4]")
    print(element.text)
    ele1=element.text.strip().split(" ")
    lis.append(ele1[0])
print(lis)
lis.sort()
print(lis)


