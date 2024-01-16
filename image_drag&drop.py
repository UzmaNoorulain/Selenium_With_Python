from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

chromeoptions=Options()
chromeoptions.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chromeoptions)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[5]/ul[2]/li[4]/a').click()

#Drag And Drop
act=ActionChains(driver)
source=driver.find_element(By.CSS_SELECTOR,'#drag1')
target=driver.find_element(By.CSS_SELECTOR,'#div1')
act.drag_and_drop(source,target).perform()