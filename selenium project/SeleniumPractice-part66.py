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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(1)
driver.find_element(By.XPATH,"//div[@id='radio-btn-example']//label[2]/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("In")
time.sleep(2)
driver.find_element(By.XPATH,"//ul[@id='ui-id-1']/li/div[text()='Equatorial Guinea']/parent::li").click()
time.sleep(3)
ele=Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
ele.select_by_visible_text("Option3")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='checkbox-example']//label[2]/input").click()
time.sleep(2)
print("the title of first page",driver.title)
driver.find_element(By.XPATH,"//button[text()='Open Window']").click()
time.sleep(2)
lis=[]
wind_ids=driver.window_handles
for wind_id in wind_ids:
    lis.append(wind_id)
driver.switch_to.window(lis[1])
print("the title of second page is",driver.title)
driver.switch_to.window(lis[0])
print("the title of first page again",driver.title)
time.sleep(3)
########tab now############
print("#############for tab ###############")
driver.find_element(By.XPATH,"//a[@id='opentab']").click()
time.sleep(2)
lis1=[]
wind_ids=driver.window_handles
for wind_id in wind_ids:
    lis1.append(wind_id)
driver.switch_to.window(lis[1])
print("the title of second page is",driver.title)
driver.switch_to.window(lis[0])
print("the title of first page again",driver.title)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("chandu")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
ele=driver.switch_to.alert
print(ele.text)
ele.accept()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("chandu")
driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
ele1=driver.switch_to.alert
print(ele.text)
ele1.accept()