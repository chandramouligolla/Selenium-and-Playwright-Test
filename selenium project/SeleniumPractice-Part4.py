#upload files
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
driver.find_element(By.XPATH,"//input[@id='singleFileInput']").send_keys(r"C:\Users\DELL\Documents\practicepagelinks.txt")
driver.find_element(By.XPATH,"//button[text()='Upload Single File']").click()
time.sleep(3)
file1=r"C:\Users\DELL\Documents\practicepagelinks.txt"
file2=r"C:\Users\DELL\Documents\demodocument.txt"
files=f"{file1}\n{file2}"
driver.find_element(By.XPATH,"//input[@id='multipleFilesInput']").send_keys(files)
driver.find_element(By.XPATH,"//button[text()='Upload Multiple Files']").click()
time.sleep(3)

