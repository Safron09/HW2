from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

XPATH_LOCATOR = (By.XPATH, "//div[@id='nav-tools']//a[@id='nav-cart']")
X_EMPTY_LOCATOR = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

@given('Go to Amazon WebPage')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@When('Click on Cart Icon')
def cart_click(context):
    search_button = context.driver.find_element(*XPATH_LOCATOR)
    search_button.click()
    sleep(2)

@Then('Check If cart is empty')
def cart_empty(context):
    assert 'Your Amazon Cart is empty' in context.driver.find_element(*X_EMPTY_LOCATOR).text



