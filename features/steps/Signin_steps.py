from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




@then('verify sign in form opened')
def verify_sign_results(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, '//span[contains(text(),"Sign into your Target account")]').text
    assert expected_text in actual_text, f'Expected {expected_text} not in actual {actual_text}'

