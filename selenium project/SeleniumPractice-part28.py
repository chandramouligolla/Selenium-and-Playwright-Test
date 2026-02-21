#custom and select dropdown
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
driver.get("https://www.qaplayground.com/practice")
driver.find_element(By.XPATH,"//span[text()='Select By']").click()
time.sleep(2)
# drp_down=driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/section/div/div/div[1]/div/div/div[1]/button")
act=ActionChains(driver)
# Enter_element=Keys.ENTER
# time.sleep(2)
# drp_down.send_keys("Grapes")
# time.sleep(2)

######2nd element############

# drp_down=Select(driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/section/div/div/div[1]/div/div/div[2]/select"))
# ele=drp_down.options
# for i in ele:
#     print(i.text)
# act.key_down(Keys.CONTROL)
# drp_down.select_by_visible_text("Ant-Man")
# drp_down.select_by_visible_text("The Avengers")
# act.key_up(Keys.CONTROL)

ele3=driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/section/div/div/div[1]/div/div/div[3]/button")
ele3.click()
time.sleep(3)
ele3.send_keys("Python")







