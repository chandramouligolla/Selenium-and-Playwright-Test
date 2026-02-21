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
driver.get("https://testerbud.com/register")
#//div[@class='mt-2 list-group list-group-flush']/div
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("Chandra@gmail.com")
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("Aaaaaaamma@1")
no_of_steps_not_done=driver.find_elements(By.XPATH,"//div[@class='mt-2 list-group list-group-flush']/div[@class='text-danger list-group-item']")
print("steps not done",len(no_of_steps_not_done))
no_of_Steps_done=driver.find_elements(By.XPATH,"//div[@class='mt-2 list-group list-group-flush']/div[@class='text-success list-group-item']")
print("steps that are done",len(no_of_Steps_done))
for i in no_of_steps_not_done:
    print(i.text)
print("################################")
for j in no_of_Steps_done:
    print(j.text)

