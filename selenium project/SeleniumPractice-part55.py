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
driver.get("https://automationtesting.co.uk/index.html")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".toggle").click()
time.sleep(2)
ele=driver.find_element(By.XPATH,"//a[text()='Predictive Search']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
ele.click()
time.sleep(5)
tit=driver.current_url
print(tit)
driver.find_element(By.XPATH,"//input[@id='myInput']").send_keys("I")
time.sleep(3)
list_of_elements=driver.find_elements(By.XPATH,"//div[@id='myInputautocomplete-list']/div")
print("Number of elements present are",len(list_of_elements))
for list_of_element  in list_of_elements:
    if list_of_element.text=="India":

        list_of_element.click()
        time.sleep(5)
#     # print(list_of_element.get_attribute("value"))
#     if list_of_element.get_attribute("value")=="India":
#        print(list_of_element.get_attribute("value"))
#        ele=driver.find_elements(By.XPATH,"//div[@id='myInputautocomplete-list']/div/input/parent::div")
#        for ele1 in ele:
#            if ele1.text=="India":
#                ele1.click()
#                time.sleep(5)
# wait = WebDriverWait(driver, 10)
# india_element = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//div[@id='myInputautocomplete-list']//input[@value='India']/parent::div")
#     )
# )
# india_element.click()
# time.sleep(5)
ele=driver.find_element(By.XPATH,"//div[@id='myInputautocomplete-list']//input[@value='India']/parent::div")
ele.click()
time.sleep(3)





