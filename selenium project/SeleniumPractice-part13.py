#dropdwon slider
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
driver.find_element(By.XPATH,"//input[@id='comboBox']").click()
all_elements=driver.find_elements(By.XPATH,"//*[@id='dropdown']/div")
for elements in all_elements:
    if elements.text=="Item 36":
        driver.execute_script("arguments[0].scrollIntoView();",elements)
        time.sleep(2)
        elements.click()
        no_of_units_dragged=driver.execute_script("return window.pageYOffset;")
        print(no_of_units_dragged)









