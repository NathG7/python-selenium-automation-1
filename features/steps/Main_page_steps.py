from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load, this can not be updated to a WAIT!
    sleep(6)


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