import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
#ops.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://automationtesting.co.uk")
time.sleep(3)
ele=driver.find_element(By.XPATH,"//a[text()='Cypress.io 10 using Javascript!']")
#driver.execute_script("arguments[0].scrollIntoView();",ele)
#driver.execute_script("window.scrollBy(0,882)","")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(3)
print(driver.execute_script("return window.pageYOffset"))
time.sleep(3)
