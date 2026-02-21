#WebTable static

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
No_of_columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")
No_of_rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
print("No of columns",len(No_of_columns))
print("No of rows",len(No_of_rows))

list_of_elements=[]
for i in range(2,len(No_of_rows)+1):
    ele=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(i)+"]/td[3]")
    #print(ele.text)
    if ele.text=="Javascript":
        author=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(i)+"]/td[2]")
        list_of_elements.append(author.text)
print(len(list_of_elements))
for list_of_element in list_of_elements:
    print("the Author for selenium are",list_of_element)

# for row in range(2, 8):
#     xpath = f"//table[@name='BookTable']/tbody/tr[{row}]/td[3]"
#     element = driver.find_element(By.XPATH, xpath)
#     print(element.text)














