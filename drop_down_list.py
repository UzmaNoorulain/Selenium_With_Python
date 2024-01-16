import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#For Dropdown Select
from selenium.webdriver.support.ui import Select

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,'Web Tables').click()

#clear text from input field
driver.find_element(By.NAME,'row-1-position').clear()
time.sleep(3)

#enter text in input field
driver.find_element(By.NAME,'row-1-position').send_keys("SDE")
time.sleep(3)

#selecting drop_down list
#select by index
d_d_list=Select(driver.find_element(By.ID,'row-1-office'))
d_d_list.select_by_index(2)
time.sleep(3)

#select by value
d_d_list1=Select(driver.find_element(By.NAME,'row-2-office'))
d_d_list1.select_by_value("New York")
time.sleep(3)

#select by Visible Text
d_d_list2=Select(driver.find_element(By.NAME,'row-3-office'))
d_d_list2.deselect_by_visible_text("London")
time.sleep(3)

#To close Window
driver.close()