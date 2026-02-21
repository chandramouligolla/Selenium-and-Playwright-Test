import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
#ops.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
ale=driver.switch_to.alert
print(ale.text)
ale.accept()
time.sleep(5)

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
ale1=driver.switch_to.alert
print(ale1.text)
time.sleep(2)
ale1.accept()
time.sleep(3)

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
ale1=driver.switch_to.alert
print(ale1.text)
time.sleep(2)
ale1.dismiss()
time.sleep(3)


driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
ale3=driver.switch_to.alert
print(ale3.text)
time.sleep(2)
ale3.send_keys("Hi i am inside the text box")
ale.accept()
ale4=driver.find_element(By.XPATH,"//p[@id='result']")
print(ale4.text)
all_ale4=ale4.text.split(":")
print(all_ale4[1])
all_ele_1=all_ale4[1].strip()
print("this is the first ele",all_ele_1)
print(type(all_ele_1))
assert all_ele_1=='Hi i am inside the text box', f'This is not the correct text i entered'












