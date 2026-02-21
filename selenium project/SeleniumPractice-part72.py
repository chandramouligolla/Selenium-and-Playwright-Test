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
driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")
time.sleep(1)
No_of_columns=driver.find_elements(By.XPATH,"//table[@class='table table-striped mt-3']/thead//th")
print(len(No_of_columns))
No_of_rows=driver.find_elements(By.XPATH,"//table[@class='table table-striped mt-3']//tbody/tr")
print(len(No_of_rows))
for i in range(1,len(No_of_rows)+1):
    ele=driver.find_element(By.XPATH,"//table[@class='table table-striped mt-3']//tbody/tr["+str(i)+"]/td[6]")
    if ele.text=="Compliance":
        ele1=driver.find_element(By.XPATH,"//table[@class='table table-striped mt-3']//tbody/tr["+str(i)+"]/td[5]")
        print("the item for it is",ele1.text)
        break


