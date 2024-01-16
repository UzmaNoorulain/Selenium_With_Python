import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()

#Retrieving the title of the current Webpage
title=driver.title
print(title)

#Retrieving the URL of the current webpage
url=driver.current_url
print(url)
time.sleep(3)
driver.close()