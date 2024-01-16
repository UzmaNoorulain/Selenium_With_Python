import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="homeSubmenu"]/li[1]/a').click()

#varifying Element is enabled or not
element=driver.find_element(By.XPATH,'//*[@id="subject"]')
if element.is_enabled():
    print("enabled")
else:
    print("not enabled")

time.sleep(4)
driver.close()