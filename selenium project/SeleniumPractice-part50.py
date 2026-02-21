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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://automationtesting.co.uk/browserTabs.html")
time.sleep(2)
curr_window=driver.current_window_handle
print("the current window id",curr_window)
driver.find_element(By.XPATH,"//input[@value='Open Tab']").click()
time.sleep(2)
all_winids=driver.window_handles
lis=[]
for all_id in all_winids:
    #print(all_id)
    lis.append(all_id)
print(lis)
driver.switch_to.window(lis[1])
driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("instagram")
time.sleep(2)

