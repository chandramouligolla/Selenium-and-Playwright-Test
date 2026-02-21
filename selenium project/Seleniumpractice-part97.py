from os import fsdecode
import time
import requests
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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationcentral.com/demo/multi_select_dropdown.html")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='dropdown-toggle']").click()
ele=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# for i in ele:
#     if i.get_attribute("value")=="Grape" or i.get_attribute("value")=="Date":
#         ancestor_element=i.find_element(By.XPATH,"./ancestor::li")
#         ancestor_element.click()
#     #print(i.get_attribute("value"))
# time.sleep(2)
# for i in ele:
#     if i.get_attribute("value")=="Grape" or i.get_attribute("value")=="Date":
#         anc_element=driver.find_element(By.XPATH,f"//input[@value='{i.get_attribute('value')}']/ancestor::li")
#         driver.execute_script("arguments[0].click();", anc_element)
#         time.sleep(2)







# ele=driver.find_elements(By.XPATH,"//ul[@id='dropdown-menu']/li")
# for i in ele:
#     if i.get_attribute("value")=="Grape" or i.get_attribute("value")=="Date":
#         i.click()

