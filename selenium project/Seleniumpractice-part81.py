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
driver.get("https://www.tutorialspoint.com/selenium/practice/accordion.php")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='headingTwentyOne']/button").click()
time.sleep(3)
driver.get("https://www.tutorialspoint.com/selenium/practice/auto-complete.php")
driver.find_element(By.XPATH,"//*[@id='tags']").send_keys("P")
time.sleep(2)
list_of_unseens=driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']//li/div")
for unseen in list_of_unseens:
    #print(unseen.text)
        if unseen.text=="Perl":
            unseen.click()
            time.sleep(3)
            