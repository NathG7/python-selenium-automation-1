from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(10)


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from the side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(6)


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://target.com/cart')


CART_SUMMARY = (By.CSS_SELECTOR, '#cart-summary-heading')


@then('Verify cart has item(s)')
def verify_cart_items(context):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    expected_text2 = 'Cart'
    assert expected_text2 in cart_summary, f'Expected{expected_text2} items but got {cart_summary}'
