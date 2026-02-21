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
driver.get("https://testautomationpractice.blogspot.com/")
actual_title=driver.title
assert actual_title=="Automation Testing Practice","actual statement is not matching with expected title"
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys('insta')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
time.sleep(2)
no_of_elements=driver.find_elements(By.XPATH,"//div[@class='wikipedia-search-results']/div/a")
print("Total number of elements:",len(no_of_elements))
driver.find_element(By.XPATH,"//div[@class='wikipedia-search-results']//a[text()='Instant-runoff voting']/parent::div").click()
time.sleep(2)
#cur_window=driver.current_window_handle
wind_ids=driver.window_handles
lis=[]
for wind_id in wind_ids:
    lis.append(wind_id)
driver.switch_to.window(lis[1])
print(driver.title)


