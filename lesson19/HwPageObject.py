from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def data():
    driver = webdriver.Chrome()
    baseUrl = 'https://the-internet.herokuapp.com'
    return [baseUrl, driver]


class Test_page_dropdown(object):

    def test_dropdown(self, data):
        method = '/dropdown'
        data[1].
        driver.get(baseUrl + method)
        dropdown = driver.find_elements_by_id('dropdown')
        assert dropdown == 1


# if __name__ == '__main__':
#     print Test_page_dropdown.test_dropdown()

# class test_page_dropdown(object):


# if __name__ == '__main__':
#     test_dropdown
#     print test_dropdown.dropdown