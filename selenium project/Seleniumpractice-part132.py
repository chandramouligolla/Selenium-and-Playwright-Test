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
ops.add_argument("--disabled-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/#")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()
year="2016"
month="June"
day="25"
while True:
    Year_element=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    month_element=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    if Year_element == year and month_element == month:
        break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]").click()
driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[7]").click()
time.sleep(3)
