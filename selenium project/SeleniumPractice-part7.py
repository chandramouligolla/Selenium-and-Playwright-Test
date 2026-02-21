#
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
No_of_rows=driver.find_elements(By.XPATH,"//table[@id='productTable']//tbody/tr")
print("number of rows:",len(No_of_rows))
No_of_columns=driver.find_elements(By.XPATH,"//table[@id='productTable']//tbody/tr[1]/td")
print("number of columns:",len(No_of_columns))
total_pag_buttons=driver.find_elements(By.XPATH,"//ul[@id='pagination']/li")
l_pagination_button=len(total_pag_buttons)
print("total pagnition buttons:",l_pagination_button)
for i in range(1,l_pagination_button+1):
    #count=1
    for j in range(1,len(No_of_rows)+1):
        ele=driver.find_element(By.XPATH,"//*[@id='productTable']//tbody/tr["+str(j)+"]/td[2]")
        print(ele.text)

    if i<l_pagination_button:
        sle_ele=driver.find_element(By.XPATH, "//ul[@id='pagination']/li["+str(i+1)+"]")
        sle_ele.click()
        #count+=1




# count=0
# count_for_button=1
# for i in range(len(No_of_rows)+1):
#     ele=driver.find_element(By.XPATH,"//table[@id='productTable']//tbody/tr["+str(i)+"]/td[2]").text
#     count+=1
#     print(ele)
#     if count>len(No_of_rows):
#         count=0
#         count_for_button+=1
#         driver.find_element(By.XPATH,"//ul[@id='pagination']/li["+str(count_for_button)+"]").click()






