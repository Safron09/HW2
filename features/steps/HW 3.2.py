from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_STRING = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.XPATH, "//input[@id='nav-search-submit-button']")
CHOOSE_ITEM = (By.XPATH, "//div[@data-asin = 'B08QD2WW4V']")
ADD_TO_CART_BUTTON = (By.XPATH, "//input[@id = 'add-to-cart-button']")
CART_BUTTON = (By.XPATH, "//div[@id='nav-tools']//a[@id='nav-cart']")
DROP_MENU = (By.XPATH, "//span[@id = 'a-autoid-0']")
DELETE_BUTTON = (By.XPATH, "//a[@id = 'dropdown1_0']")
EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")
CART_BUTTON2 = (By.XPATH, "//div[@id='nav-tools']//a[@id='nav-cart']")


@given('Go to Amazon')
def go_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Enter {search_text}')
def search_string(context, search_text):
    search_string = context.driver.find_element(*SEARCH_STRING)
    search_string.clear()
    search_string.send_keys(search_text)

@when('Click Enter')
def click_search(context):
    click_search = context.driver.find_element(*SEARCH_BUTTON)
    click_search.click()
    sleep(1)

@when('Choose Item and Click on it')
def item_click(context):
    item_click = context.driver.find_element(*CHOOSE_ITEM)
    item_click.click()
    sleep(1)

@then('Add Item to the cart')
def cart_item(context):
    cart_item = context.driver.find_element(*ADD_TO_CART_BUTTON)
    cart_item.click()
    sleep(1)

@then('Go to Cart')
def cart_click(context):
    search_button = context.driver.find_element(*CART_BUTTON)
    search_button.click()
    sleep(1)

@then ('DropDown Menu open')
def change_qua(context):
    change_qua = context.driver.find_element(*DROP_MENU)
    change_qua.click()
    sleep(1)

@then('Change to zero')
def delete_item(context):
    delete_item = context.driver.find_element(*DELETE_BUTTON)
    delete_item.click()
    sleep(1)

@then('Check Cart')
def check_cart(context):
    search_button = context.driver.find_element(*CART_BUTTON2)
    search_button.click()
    sleep(1)

@then('Verify that Cart is Empty')
def cart_empty(context):
    assert 'Your Amazon Cart is empty' in context.driver.find_element(*EMPTY_CART).text
    sleep(2)


