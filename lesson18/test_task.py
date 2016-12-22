import pytest
from selenium import webdriver

# class TestLogin:

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/')
    link_auth = driver.find_elements_by_link_text('Form Authentication')
    # print link_auth
    link_auth[0].click()
    username_field = driver.find_element_by_id('username')
    password_field = driver.find_element_by_id('username')
    driver.quit()
