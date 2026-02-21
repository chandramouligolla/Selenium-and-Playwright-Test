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
driver.get("file:///C:/Users/DELL/PycharmProjects/htmlproject/Sliders.html")
time.sleep(2)
slider1=driver.find_element(By.XPATH,"//input[@id='volumeSlider']")
act=ActionChains(driver)
act.drag_and_drop_by_offset(slider1,100,0).perform()
slider2=driver.find_element(By.XPATH,"//*[@id='brightnessSlider']")
act.drag_and_drop_by_offset(slider2,-100,0).perform()
time.sleep(10)

