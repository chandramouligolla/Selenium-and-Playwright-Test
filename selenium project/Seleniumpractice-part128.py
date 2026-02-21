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
ele=driver.find_element(By.XPATH,"//*[@id='singleFileInput']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
ele.send_keys(r"C:\Users\DELL\Downloads\info.txt")
driver.find_element(By.XPATH,"//*[@id='singleFileForm']/button").click()
time.sleep(2)
ele2=driver.find_element(By.XPATH,"//*[@id='multipleFilesInput']")
driver.execute_script("arguments[0].scrollIntoView();",ele2)
ele2.send_keys(r"C:\Users\DELL\Downloads\info.txt")
ele2.send_keys(r"C:\Users\DELL\Downloads\practicepagelinks.txt")
driver.find_element(By.XPATH,"//*[@id='multipleFilesForm']/button").click()
time.sleep(3)


