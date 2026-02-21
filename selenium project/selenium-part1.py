import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
#ops.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
# driver.find_element(By.XPATH,"//span[text()='Admin']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active' and @placeholder='Search']").send_keys("P")
list_of_searched_elements=driver.find_elements(By.XPATH,"//div[@id='app']/div[1]/div[1]/aside//ul//span")
for list_in_searched_element in list_of_searched_elements:
    print(list_in_searched_element.text)
    if list_in_searched_element.text=="Performance":
        list_in_searched_element.click()
time.sleep(5)
driver.quit()