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
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/selenium_practice_page.html")
time.sleep(2)
ele2=driver.find_elements(By.XPATH,"//div[@id='link-testing']//div/a")
count=0
for ele in ele2:
    urls=ele.get_attribute('href')
    print(urls)
    res=requests.head(urls)
    print(res.status_code)
    if res.status_code>=400:
        print(urls, "is a broken link")
        count+=1



