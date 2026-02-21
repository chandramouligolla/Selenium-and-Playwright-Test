import time
from datetime import datetime
from email.utils import format_datetime
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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://www.qaplayground.com/practice")
driver.find_element(By.XPATH,"//span[text()='Click']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Go To Home']").click()
time.sleep(2)
print(driver.title)
driver.back()
print(driver.title)
ele1=driver.find_element(By.XPATH,"//button[text()='Find Location']")
ele2=ele1.location
print(ele2)
ele3=driver.find_element(By.XPATH,"//button[text()='Find my color?']")
print(ele3.value_of_css_property("color"))
ele4=driver.find_element(By.XPATH,"//button[text()='Do you know my size?']")
print(ele4.size)
ele5=driver.find_element(By.ID,"button-disabled")
print(ele5.is_enabled())
time.sleep(2)
ele6=driver.find_element(By.XPATH,"//button[text()='Click and Hold!']")
act=ActionChains(driver)
time.sleep(2)
act.click_and_hold(ele6).perform()
time.sleep(1.5)
act.release(ele6).perform()
ele7=driver.find_element(By.XPATH,"//button[text()='Double Click Me']")
act.double_click(ele7).perform()
time.sleep(5)
ele8=driver.find_element(By.XPATH,"//button[text()='Right Click Me']")
act.context_click(ele8).perform()
time.sleep(5)






