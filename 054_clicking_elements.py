from selenium import webdriver
from time import sleep



driver = webdriver.Chrome('/home/py/Apps/chromedriver')

# open instagram.com -- > url --> https://www.instagram.com

driver.get('https://www.instagram.com')

sleep(5)

login_button = driver.find_element_by_link_text('Log in')

login_button.click()

sleep(5)


driver.close()