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
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
time.sleep(1)
driver.find_element(By.ID,"name").send_keys("Chandra")
driver.find_element(By.NAME,"email").send_keys("mouli")
driver.find_element(By.ID,"gender").click()
driver.find_element(By.XPATH,"//*[@id='mobile']").send_keys("8008505587")
driver.find_element(By.XPATH,"//*[@id='dob']").send_keys("02051998")
driver.find_element(By.ID,"subjects").send_keys("English")
driver.find_element(By.XPATH,"//*[@id='hobbies']").click()
driver.find_element(By.ID,"picture").send_keys(r"C:\Users\DELL\Downloads\info.txt")
driver.find_element(By.XPATH,"//textarea[@id='picture']").send_keys("2-33/1, rangarajupeta")
time.sleep(3)
Ele=Select(driver.find_element(By.XPATH,"//select[@id='state']"))
Ele.select_by_visible_text("Haryana")
time.sleep(2)
ele2=Select(driver.find_element(By.ID,"city"))
ele2.select_by_visible_text("Lucknow")
time.sleep(3)



