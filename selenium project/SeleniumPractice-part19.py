#iframes

import time
from datetime import datetime
from email.utils import format_datetime


import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://automationtesting.co.uk/iframes.html")
print(driver.title)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".toggle").click()
ele=driver.find_element(By.XPATH,"//*[@id='main']/div/div[1]/div/iframe")
driver.switch_to.frame(ele)
driver.find_element(By.XPATH,"//*[@id='sidebar']/a").click()
time.sleep(2)
#driver.switch_to.default_content()
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,"//*[@id='sidebar']/a").click()
time.sleep(2)


#ele=driver.find_element(By.XPATH,"//*[@id='main']/div/div[1]/div/iframe")


# driver.switch_to.frame(0)
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='sidebar']/a").click()
# time.sleep(2)
# #driver.switch_to.default_content()
# driver.switch_to.parent_frame()
# driver.find_element(By.XPATH,"//*[@id='sidebar']/a").click()
# time.sleep(2)
# driver.switch_to.frame(1)
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='movie_player']/div[5]/button").click()
# time.sleep(3)


