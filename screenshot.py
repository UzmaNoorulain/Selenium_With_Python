from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=W=webdriver.Chrome(options=chrome_options)

#capturing Screenshot
driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()
driver.save_screenshot("F:\\puthon\\screenshot\\.png")