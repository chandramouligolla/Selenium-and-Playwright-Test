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
driver.get("https://automationtesting.co.uk/tables.html")
time.sleep(2)
No_of_columns=driver.find_elements(By.XPATH,"//*[@id='main']/div/div[1]/div/table/thead/tr/th")
print(len(No_of_columns))
No_of_rows=driver.find_elements(By.XPATH,"//*[@id='main']/div/div[1]/div/table/tbody/tr")
print(len(No_of_rows))
for i in range(1,len(No_of_rows)):
    ele=driver.find_element(By.XPATH,"//*[@id='main']/div/div[1]/div/table/tbody/tr["+str(i)+"]/td[6]")
    #print(ele.text)
    if ele.text=="Student":
        ele1 = driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/table/tbody/tr[" + str(i) + "]/td[5]")
        ele2= driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/table/tbody/tr[" + str(i) + "]/td[4]")
        print(ele.text, "",ele1.text,"",ele2.text)
time.sleep(3)



