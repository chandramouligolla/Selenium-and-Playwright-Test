import requests
import time
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
driver.get("https://automationtesting.co.uk/iframes.html")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='sidebar']/a").click()
driver.find_element(By.XPATH,"//*[@id='sidebar']/a").click()
ele=driver.find_element(By.XPATH,"//iframe[@src='index.html']")
driver.switch_to.frame(ele)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/a").click()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='sidebar']/a").click()
time.sleep(3)
ele1=driver.find_element(By.XPATH,"//iframe[@src='https://www.youtube.com/embed/jNQXAC9IVRw']")
driver.switch_to.frame(ele1)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='movie_player']/div[5]/button").click()
time.sleep(2)



