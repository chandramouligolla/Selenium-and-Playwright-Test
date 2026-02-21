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
driver.get("https://www.tutorialspoint.com/selenium/practice/select-menu.php")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='mbsc-control-0']/div/label/span[2]/span[1]").click()
time.sleep(2)
ele1=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[43]")
ele2=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[47]")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).perform()
ele1.click()
#ele=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div")
ele=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div")
time.sleep(2)
act.drag_and_drop_by_offset(ele,0,100).perform()
#ele.click()
ele2.click()
act.key_up(Keys.CONTROL).perform()
time.sleep(3)


