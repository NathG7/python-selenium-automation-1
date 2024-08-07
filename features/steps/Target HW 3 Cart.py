from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('click on cart')
def click_cart(context):
    # click on cart
    context.driver.find_element(By.CSS_SELECTOR, "use[href*='/icons/Cart']").click()
    sleep(6)

@then('verify cart is empty')
def verify_cart_results(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f'Expected {expected_text} not in actual {actual_text}'

