from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open target main page')
def open_target(context):
    context.app.main_page.open()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search()


@when('click on cart')
def click_cart(context):
    # click on cart
    context.driver.find_element(By.CSS_SELECTOR, "use[href*='/icons/Cart']").click()
    #sleep(10)


@when('click sign in')
def click_signin(context):
    # click on signin
    context.driver.find_element(By.XPATH, '//span[contains(text(),"Sign in")]').click()
    #sleep(10)


@when('click on right nav sign in')
def click_signin_right(context):
    #another
    context.driver.find_element(By.XPATH, '//a[@data-test="accountNav-signIn"]').click()
    #sleep(10)