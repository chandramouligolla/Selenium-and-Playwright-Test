#dynamic web tables

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
No_Of_Column=driver.find_elements(By.XPATH,"//table[@id='taskTable']/tbody/tr")
No_of_rows=driver.find_elements(By.XPATH,"//table[@id='taskTable']/tbody/tr")
print("the no of columns are",len(No_Of_Column))
print("the no of rows are",len(No_of_rows))
i_number=[]
for i in range(1,len(No_of_rows)+1):
    ele=driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr["+str(i)+"]/td[5]").text
    e_str=ele.split(" ")
    print("the speed",e_str[0])
    print("the speed unit",e_str[1])
    print("the type of speed",type(e_str[0]))
    i_number.append(float(e_str[0].strip()))

for i in i_number:
    print(i)
    print("the type",type(i))
minimum_number=min(i_number)
print("the minimum number is",minimum_number)
i_number.sort()
print("Sorted speeds:", i_number)
print("the second number",i_number[1])




