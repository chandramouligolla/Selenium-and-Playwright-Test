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
driver.get("https://testautomationpractice.blogspot.com/#")
time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='start-date']").send_keys("07-30-2016")
# time.sleep(3)
No_of_columns=driver.find_elements(By.XPATH,"//table[@id='productTable']/thead/tr/th")
print(len(No_of_columns))
No_of_rows=driver.find_elements(By.XPATH,"//table[@id='productTable']/tbody/tr")
print(len(No_of_rows))
NO_of_pagn=driver.find_elements(By.XPATH,"//ul[@id='pagination']/li")
print(len(NO_of_pagn))
# for j in range(1,len(NO_of_pagn)+1):
#     for i in range(1,len(No_of_rows)+1):
#         ele=driver.find_element(By.XPATH,"//table[@id='productTable']/tbody/tr["+str(i)+"]/td[2]")
#         print(ele.text)
#         time.sleep(2)
#         if len(NO_of_pagn)<=5:
#             driver.find_element(By.XPATH,"//ul[@id='pagination']/li["+str(j)+"]").click()
for i  in range(1,len(NO_of_pagn)+1):
    for j in range(1,len(No_of_rows)+1):
        ele=driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr["+str(j)+"]/td[2]")
        print(ele.text)
    if i!=len(NO_of_pagn):
      driver.find_element(By.XPATH, "//ul[@id='pagination']/li[" + str(i+1) + "]").click()




