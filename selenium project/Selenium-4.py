import time

from requests.packages import target
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.expected_conditions import alert_is_present
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
#ops.add_argument("--headless=new")
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://automationtesting.co.uk/actions.html")
time.sleep(3)
sour_ele=driver.find_element(By.XPATH,"//div[@class='droptarget']/p")
print(sour_ele.text)
target_ele=driver.find_element(By.XPATH,"/html//body/div/div[1]/div/div[1]/div/div[2]")
act=ActionChains(driver)
act.drag_and_drop(sour_ele,target_ele).perform()
time.sleep(2)
doubleclick=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/p")
act.double_click(doubleclick).perform()
time.sleep(3)
ele_for_shift=driver.find_element(By.XPATH,"//div[@id='wrapper']/div/div/div[2]/div[2]/div/div/div/p")
time.sleep(2)
act.key_down(Keys.SHIFT).click(ele_for_shift).key_up(Keys.SHIFT).perform()
time.sleep(2)
alert_window=driver.switch_to.alert
print(alert_window.text)
alert_window.accept()





