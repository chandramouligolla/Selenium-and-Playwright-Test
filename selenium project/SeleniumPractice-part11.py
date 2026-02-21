#windows

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
driver.find_element(By.XPATH,"//button[@id='PopUp']").click()
win_id=driver.window_handles
id=[]
for win in win_id:
    print("the window is ", win)
    id.append(win)
driver.switch_to.window(id[1])
print("the title of child window is",driver.title)
driver.switch_to.window(id[2])
print("the title of 2nd child window is",driver.title)
driver.switch_to.window(id[0])
print("the title of parent window is",driver.title)