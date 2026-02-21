import time
from datetime import datetime
from email.utils import format_datetime
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://artoftesting.com/samplesiteforselenium")
time.sleep(5)
drp_down=Select(driver.find_element(By.XPATH,"//select[@id='testingDropdown']"))
drp_down.select_by_visible_text("Manual Testing")
element=driver.find_element(By.XPATH,"//select[@id='testingDropdown']")
driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(2)
all_options=drp_down.options
for all_option in all_options:
    print(all_option.text)


########alert box########
driver.find_element(By.XPATH,"//button[text()='Generate Alert Box']").click()
time.sleep(2)
te_element1=driver.switch_to.alert
print(te_element1.text)
te_element1.accept()
driver.find_element(By.XPATH,"//button[text()='Generate Confirm Box']").click()
time.sleep(2)
te_element2=driver.switch_to.alert
print(te_element2.text)
te_element1.accept()

#drag and drop
time.sleep(5)
source=driver.find_element(By.XPATH,"//div[@id='targetDiv']")
target=driver.find_element(By.XPATH,"//*[@id='myImage']")
act=ActionChains(driver)
time.sleep(2)
act.drag_and_drop(target,source).perform()
time.sleep(3)