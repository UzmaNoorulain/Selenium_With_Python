import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[5]/ul[2]/li[4]/a').click()

#Retrieving the text between HTML Tags
txt=driver.find_element(By.CSS_SELECTOR,'#content > p').text
print(txt)
time.sleep(3)
driver.quit()

