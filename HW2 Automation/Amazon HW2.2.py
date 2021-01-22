from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

search_button = driver.find_element(By.XPATH,"//div[@id= 'nav-tools']//a[@id= 'nav-orders']")

search_button.click()
sleep(5)
assert 'Sign-In' in driver.find_element(By.XPATH, "//div[@class= 'a-box-inner a-padding-extra-large']/h1").text

driver.quit()
