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
driver.get("https://www.tutorialspoint.com/selenium/practice/date-picker.php")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='datetimepicker1']").click()
day="June 25, 1998"
month="June"
drp_down=Select(driver.find_element(By.XPATH,"//select[@class='flatpickr-monthDropdown-months']"))
drp_down.select_by_visible_text(month)
while True:
    com_year=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div/span[26]")
    var=com_year.get_attribute("aria-label")
    if var==day:
        break
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/span[2]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div/span[26]").click()
time.sleep(3)
tim="09"
#for i in range(3):
 #   driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/span[1]").click()
ele1=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/input")
ele1.send_keys("09")
act=ActionChains(driver)
act.send_keys(Keys.ENTER).perform()
time.sleep(3)
ele=driver.find_element(By.XPATH,"//*[@id='datetimepicker1']").text
print(ele)