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
driver.get("https://teststore.automationtesting.co.uk/index.php")
driver.find_element(By.XPATH,"//*[@id='search_widget']/form/input[2]").send_keys("Hum")
time.sleep(7)
driver.find_element(By.XPATH,"//*[@id='ui-id-1']/li/a/span[text()='Hummingbird cushion']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='input-group-btn-vertical']//i[@class='material-icons touchspin-up']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button").click()
driver.find_element(By.XPATH,"//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button").click()
time.sleep(2)
time.sleep(3)
driver.find_element(By.XPATH,"//a[@href='//teststore.automationtesting.co.uk/index.php?controller=cart&action=show' and @class='btn btn-primary']").click()
time.sleep(2)
assert driver.current_url=='https://teststore.automationtesting.co.uk/index.php?controller=cart&action=show',"assertion error"
time.sleep(2)
ele= driver.find_element(By.XPATH,"//input[@class='js-cart-line-product-quantity form-control']")
assert ele.get_attribute('value')=='2',"not the thing given"
ele=driver.find_element(By.XPATH,"//div[@class='cart-summary-line cart-total']/span[2]").text
print(ele)
ele1=ele.split("$")
print(ele1[1])


