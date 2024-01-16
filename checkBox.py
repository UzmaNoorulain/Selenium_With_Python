import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,'#homeSubmenu > li:nth-child(2) > a').click()
#driver.find_element(By.TAG_NAME,'input').click()

#Varifying is check box is selected or not
chx=driver.find_element(By.XPATH,'//*[@id="myCheck"]')
if chx.is_selected():
    pass
else:
    chx.click()
chx2=driver.find_element(By.CSS_SELECTOR,'#myCheck')
if chx2.is_selected():
    pass
else:
    chx2.click()
