import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
#ops.add_argument("--headless=new")
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://automationtesting.co.uk")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,".toggle").click()
table_ele=driver.find_element(By.XPATH,"//a[text()='Tables']")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView();",table_ele)
time.sleep(5)
print(driver.execute_script("return window.pageYOffset"))
time.sleep(2)
table_ele.click()
time.sleep(2)
list_of_headers=driver.find_elements(By.XPATH,"//table[@class='sortable']/thead/tr/th")
for headers in list_of_headers:
    print(headers.text)

No_of_columns=len(list_of_headers)
print("No of columns",No_of_columns)
No_of_rows=driver.find_elements(By.XPATH,"//div[@class='col-12 col-12-medium']//table//tbody/tr")
print("No of rows",(len(No_of_rows)))
for i in range(len(No_of_rows)):#done in company lap
    ele=driver.find_element(By.XPATH,"//div[@class='col-12 col-12-medium']//table//tbody/tr["+str(i)+"]/td[6]")
    # for j in range(len(No_of_rows)):
    #     driver.find_element(By.XPATH,"//div[@class='col-12 col-12-medium']//table//tbody/tr["+str(j)+"]")
    if ele.text=="Adminstrator":
        print(ele.text)
        break






