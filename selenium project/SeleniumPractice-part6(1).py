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
    map_value=float(e_str[0].strip())
    i_number.append((i,map_value))
for j in i_number:
    print(j)
min_tuple=i_number[0]
for item in i_number[1:]:
    if item[1]<min_tuple[1]:
        min_tuple=item
print("the min tuple",min_tuple)
min_tuple_row=min_tuple[0]
min_tuple_value=min_tuple[1]
disk_value=driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr["+str(min_tuple_row)+"]/td[4]")
print("the related disk vlue",disk_value.text)
ele1=driver.find_element(By.XPATH,"//div[@id='displayValues']/p[1]")
ele2=driver.find_element(By.XPATH,"//div[@id='displayValues']/p[2]")
ele3=driver.find_element(By.XPATH,"//div[@id='displayValues']/p[3]")
ele4=driver.find_element(By.XPATH,"//div[@id='displayValues']/p[4]")
print(ele1.text)
print(ele2.text)
print(ele3.text)
print(ele4.text)



