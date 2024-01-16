from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/brightqa3.html")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="homeSubmenu"]/li[1]/a').click()
driver.find_element(By.NAME,'firstname').send_keys("Uzma")
driver.find_element(By.ID,'lname').send_keys("Noorulain")
driver.find_element(By.XPATH,'//*[@id="content"]/div/form/div[5]/input').click()