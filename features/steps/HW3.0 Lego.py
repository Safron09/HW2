from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON_LOCATOR = (By.ID, 'nav-search-submit-button')
HEADER_CHECK_LOCATOR = (By.XPATH, "//span[@class= 'a-color-state a-text-bold']")

@given('Open Amazon web page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')

@when('Fill input string {search_text}')
def search_input(context, search_text):
    search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    search_input.clear()
    search_input.send_keys(search_text)


@When ('Click Search button')
def click_search(context):
    search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    search_button.click()
    sleep(2)

@then ('Verify that It searched for {search_text}')
def check_name(context, search_text):
    assert 'Lego' in context.driver.find_element(*HEADER_CHECK_LOCATOR).text, f'Expected "Lego", but got {search_text}'








