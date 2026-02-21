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
driver.get("https://automationtesting.co.uk/calculator.html")
driver.find_element(By.XPATH,"//*[@id='main']/div/div/div/table/tbody/tr[4]/td[3]/input").click()
driver.find_element(By.XPATH,"//*[@id='main']/div/div/div/table/tbody/tr[2]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='main']/div/div/div/table/tbody/tr[2]/td[3]/input").click()
driver.find_element(By.XPATH,"//*[@id='main']/div/div/div/table/tbody/tr[5]/td[3]/input").click()
time.sleep(1)
# result=driver.find_element(By.XPATH,"//*[@id='result']")
# print(result.text)
# time.sleep(3)
