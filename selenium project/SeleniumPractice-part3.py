#date and time pickers

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
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
Year="2026"
Month="June"
day="25"
while True:
    year_element=driver.find_element(By.CSS_SELECTOR,".ui-datepicker-year").text
    month_element=driver.find_element(By.CSS_SELECTOR,".ui-datepicker-month").text
    if year_element==Year and month_element==Month:
        break
    else:
        driver.find_element(By.XPATH,"//div[@id='ui-datepicker-div']/div/a[2]").click()

date_element=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody//td/a")
for i in date_element:
    if i.text==day:
        time.sleep(2)
        i.click()
        time.sleep(2)

#2nd date dropdown
driver.find_element(By.XPATH,"//input[@id='txtDate']").click()
month_element1=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
month_element1.select_by_visible_text("Jun")
Year_element1=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
Year_element1.select_by_visible_text("2026")
date_element=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody//td/a")
for i in date_element:
    if i.text==day:
        time.sleep(2)
        i.click()
        time.sleep(2)

#third date picker
start_date="12-10-2005"
end_date="13-10-2005"
dateformat="%d-%m-%Y"
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='start-date']").send_keys(start_date)
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='end-date']").send_keys(end_date)
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
text_for_ddiff=driver.find_element(By.XPATH,"//div[@id='result']").text
print("the value which is coimg in automation",text_for_ddiff)
start=datetime.strptime(start_date,dateformat)
end=datetime.strptime(end_date,dateformat)
date_difference=end-start
print("Date difference in days",date_difference.days)
original_diff=f"You selected a range of {date_difference.days} days."
print("the original diff",original_diff)
print("automation diff",text_for_ddiff.strip())
if text_for_ddiff.strip()==original_diff:
    print("its working")
else:
    print("mismatched")



