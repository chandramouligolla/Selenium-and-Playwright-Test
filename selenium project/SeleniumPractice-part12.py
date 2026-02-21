#mousehover actions

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
time.sleep(2)
ele=driver.find_element(By.XPATH,"//button[text()='Point Me']")
act=ActionChains(driver)
act.move_to_element(ele).perform()
time.sleep(2)
ele1=driver.find_element(By.XPATH,"//div[@class='dropdown']/div/a[2]")
time.sleep(2)
act.move_to_element(ele1).click(ele1).perform()
time.sleep(2)




