#dynamic sending and selecting from tabs

import time
from datetime import datetime
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
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("dsa")
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
time.sleep(2)
No_of_search_results=driver.find_elements(By.XPATH,"//div[@class='wikipedia-search-results']/div")
result=len(No_of_search_results)
print("No of results are",result)
result=len(No_of_search_results)
for i in range(1,result+1):
    ele=driver.find_element(By.XPATH,"//div[@class='wikipedia-search-results']/div["+str(i)+"]/a")
    if ele.text=="DSA-110":
        ele.click()
        time.sleep(2)


