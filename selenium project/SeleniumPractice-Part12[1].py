#double click and drag and drop and slider
import time
from datetime import datetime
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
ele=driver.find_element(By.XPATH,"//input[@id='field1']")
ele.clear()
ele.send_keys("Diwali")
ele1=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
act=ActionChains(driver)
act.double_click(ele1).perform()
time.sleep(2)


#drag and drop
source_ele=driver.find_element(By.CSS_SELECTOR,"div#draggable")
destination_element=driver.find_element(By.CSS_SELECTOR,"div#droppable")
act.drag_and_drop(source_ele,destination_element).perform()
time.sleep(2)

#slider
min_slider=driver.find_element(By.XPATH,"//div[@id='slider-range']//span[1]")
max_slider=driver.find_element(By.XPATH,"//div[@id='slider-range']//span[2]")
print(min_slider.location)
print(max_slider.location)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,200,0).perform()
print("...........after siding..............")
print(min_slider.location)
print(max_slider.location)
act.drag_and_drop_by_offset(min_slider,-10,0).perform()
act.drag_and_drop_by_offset(max_slider,-20,0).perform()
print("...........after negative siding..............")
print(min_slider.location)
print(max_slider.location)



