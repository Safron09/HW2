from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

search_button = driver.find_element(By.XPATH, "//li[@class= 'nav_last']/a[@class= 'nav_a'][text()= 'Help']")
search_button.click()
sleep(2)

search = driver.find_element(By.XPATH, "//div[@class= 'a-search a-span12']/input[@id= 'helpsearch']")
search.send_keys('cancel item\n')

assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class= 'help-content']").text
sleep(5)
driver.quit()