#all dropdown elements

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
drp_down1=Select(driver.find_element(By.XPATH,"//select[@id='country']"))
all_options=drp_down1.options
for all_option in all_options:
    print(all_option.text)
#drp_down1.select_by_visible_text("United Kingdom")
#drp_down1.select_by_value("germany")
drp_down1.select_by_index(1)
time.sleep(2)
ele1=Select(driver.find_element(By.XPATH,"//*[@id='colors']"))
# for sel_by_th in sel_by_ths:
#     if sel_by_th.text=="Yellow":
#         sel_by_th.click()
#         time.sleep(3)
ele1.select_by_visible_text("White")
time.sleep(2)
ele2=Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
ele2.select_by_visible_text("Giraffe")
time.sleep(2)


