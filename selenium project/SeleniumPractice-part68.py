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
act=ActionChains(driver)
ele=driver.find_element(By.XPATH,"//button[@id='mousehover']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
act.move_to_element(ele).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='mouse-hover-content']/a[text()='Top']").click()
time.sleep(2)
ele2="//*[@id='root']/div[2]/nav/div/div/div[2]/a[3]"
driver.switch_to.frame("courses-iframe")
driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.XPATH,ele2))
time.sleep(2)
driver.find_element(By.XPATH,ele2).click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div[2]/nav/div/div/div[2]/a[1]").click()
time.sleep(2)
