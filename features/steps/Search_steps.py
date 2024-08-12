from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Verify search results show for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_text, f'Expected {product} not in actual {actual_text}'