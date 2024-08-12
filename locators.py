from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#Find by ID with CSS
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
#Find by ID with CSS with tag
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")

#Find by classes, 2 are in this example
driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")

#Find by attribute
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")

#Find with multiple attributes
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][type='text']")

#Find by tag + attribute
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon']")


#Find by attribute partial
driver.find_element(By.CSS_SELECTOR, "[placeholder*='earch Ama']")



