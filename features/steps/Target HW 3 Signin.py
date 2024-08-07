from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('click sign in')
def click_signin(context):
    # click on signin
    context.driver.find_element(By.XPATH, '//span[contains(text(),"Sign in")]').click()

    sleep(10)
@when('click on right nav sign in')
def click_signin_right(context):
    #another
    context.driver.find_element(By.XPATH, '//a[@data-test="accountNav-signIn"]').click()
    sleep(10)
@then('verify sign in form opened')
def verify_sign_results(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, '//span[contains(text(),"Sign into your Target account")]').text
    assert expected_text in actual_text, f'Expected {expected_text} not in actual {actual_text}'

