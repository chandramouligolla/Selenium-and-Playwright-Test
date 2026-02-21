#tabs


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
driver.find_element(By.XPATH,"//button[text()='New Tab']").click()
window_ids=driver.window_handles
ids=[]
for window_id in window_ids:
    print("the window is ",window_id)
    ids.append(window_id)

driver.switch_to.window(ids[1])
print("the title of child window is",driver.title)
driver.switch_to.window(ids[0])
print("the title of parent window is",driver.title)



