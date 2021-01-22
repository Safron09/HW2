from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_button = driver.find_element(By.XPATH, "//input[@id= 'nav-search-submit-button']")

search.clear()
search.send_keys('Lego')

search_button.click()
assert 'Lego' in driver.find_element(By.XPATH, "//span[@class= 'a-color-state a-text-bold']").text

driver.quit()