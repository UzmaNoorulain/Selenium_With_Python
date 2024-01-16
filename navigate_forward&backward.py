import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

#Navigate Forward and Backward
driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()
time.sleep(2)
driver.get("https://omayo.blogspot.com/")
driver.back()
time.sleep(2)
driver.forward()
driver.quit()