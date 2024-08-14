from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open Circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {number} cells')
def verify_10cells(context, number):
    number = int(number)
    cells = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="@web/slingshot-components/CellsComponent/Link"]')
    assert len(cells) == number, f'Expected {number} cells, got {len(cells)}'

