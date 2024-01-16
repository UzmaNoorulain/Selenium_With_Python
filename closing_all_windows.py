import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,'#sidebar > ul > li:nth-child(4) > ul:nth-child(3) > li:nth-child(1) > a').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="content"]/button[1]').click()
time.sleep(3)

driver.quit()