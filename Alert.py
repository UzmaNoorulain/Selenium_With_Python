import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()

#Alert
driver.find_element(By.CSS_SELECTOR,'#sidebar > ul > li:nth-child(4) > ul:nth-child(3) > li:nth-child(2) > a').click()

#JavaScript Alert
driver.find_element(By.XPATH,'//*[@id="content"]/button[1]').click()
Alert=driver.switch_to.alert
time.sleep(2)
Alert.accept()

#JavaScript Confirm Box
driver.find_element(By.XPATH,'//*[@id="content"]/button[2]').click()
Alert1=driver.switch_to.alert
time.sleep(2)
Alert1.accept()

#JavaScript Prompt
driver.find_element(By.XPATH,'//*[@id="content"]/button[3]').click()
Alert2=driver.switch_to.alert
driver.switch_to.alert.send_keys("Noorulain")
time.sleep(2)
Alert2.accept()