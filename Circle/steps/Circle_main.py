from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {number} cells')
def verify_10cells(context, number):
    number = int(number)
    cells = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="@web/slingshot-components/CellsComponent/Link"]')
    assert len(cells) == number, f'Expected {number} cells, got {len(cells)}'

