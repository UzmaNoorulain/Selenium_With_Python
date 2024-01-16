import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="homeSubmenu"]/li[3]/a').click()
#Selecting radio button
rd1=driver.find_element(By.ID,'noCheck')
if rd1.is_selected():
    pass
else:
    rd1.click()
time.sleep(3)
rd2=driver.find_element(By.ID,'yesCheck')
if rd2.is_selected():
    pass
else:
    rd2.click()