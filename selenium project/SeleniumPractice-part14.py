#lables and links
import time
from datetime import datetime
from email.utils import format_datetime

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
all_elements=driver.find_elements(By.XPATH,"//*[@id='mobiles']/label")
for all_element in all_elements:
    print(all_element.text)
all_links=driver.find_elements(By.XPATH,"//*[@id='laptops']/a")
for all_link in all_links:
    print(all_link.text)