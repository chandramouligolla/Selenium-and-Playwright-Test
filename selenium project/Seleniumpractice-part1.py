#text boxes and buttons and radio buttons
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("chandra")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("chandra@gmail.com")
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9490207777")
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("2-33/1,rangarajupet")
driver.find_element(By.XPATH,"//input[@id='male']").click()
time.sleep(2)
list_of_days_labels=driver.find_elements(By.XPATH,"//*[@id='post-body-1307673142697428135']/div[4]/div/label")
print("This are the no of lists",len(list_of_days_labels))
for list_of_day in list_of_days_labels:
    print("This are the names of weekdays",list_of_day.text)
list_of_days_inputs=driver.find_elements(By.XPATH,"//*[@id='post-body-1307673142697428135']/div[4]/div/input")
# for list_of_days_in in list_of_days_ins:
#     list_of_days_in.click()
for list_of_days_input in list_of_days_inputs:
    if list_of_days_input.get_attribute('value')=='tuesday' or list_of_days_input.get_attribute('value')=='friday':
        time.sleep(2)
        list_of_days_input.click()








