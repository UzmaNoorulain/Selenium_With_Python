import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,'#homeSubmenu > li:nth-child(5) > a').click()

#For Double Click
act=ActionChains(driver)
menu=driver.find_element(By.XPATH,'//*[@id="content"]/button[1]')
act.double_click(menu).perform()
time.sleep(3)

#For Click Me
menu2=driver.find_element(By.CSS_SELECTOR,'#content > button:nth-child(5)')
act.click(menu2).perform()
time.sleep(3)

#For Right Click
menu3=driver.find_element(By.XPATH,'//*[@id="content"]/button[3]')
act.context_click(menu3).perform()