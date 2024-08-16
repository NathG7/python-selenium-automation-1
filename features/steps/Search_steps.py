from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@then('Verify search results show for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_text()


@then ('Verify correct search results URL opens for {product}')
def verify_url(context, product):
    context.app.search_results_page.verify_url()
