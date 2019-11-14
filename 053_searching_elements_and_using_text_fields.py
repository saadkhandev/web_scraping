from selenium import webdriver
from time import sleep



driver = webdriver.Chrome('/home/py/Apps/chromedriver')
driver.get('https://www.google.com')

# search tag using id

search_bar = driver.find_element_by_class_name('gLFyf')

# input data


search_bar.send_keys('I want to learn web scraping')


# submit the form

search_bar.submit()


driver.close()
