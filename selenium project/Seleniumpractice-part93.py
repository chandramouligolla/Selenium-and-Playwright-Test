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
driver.get("https://testautomationcentral.com/demo/frames_iframes.html")
time.sleep(2)
driver.switch_to.frame(0)
print(driver.title)
driver.switch_to.default_content()
print(driver.title)
cookies=driver.get_cookies()
print(cookies)
for i in cookies:
    print(i.get("expiry"))
driver.add_cookie({"name":"1","value":"2"})
cookies=driver.get_cookies()
print(cookies)
driver.delete_cookie("1")
cookies=driver.get_cookies()
print(cookies)
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(cookies)



