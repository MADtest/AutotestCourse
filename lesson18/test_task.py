import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
#
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get('https://the-internet.herokuapp.com/')
#     link_auth = driver.find_elements_by_link_text('Form Authentication')
#     # print link_auth
#     link_auth[0].click()
#     username_field = driver.find_element_by_id('username')
#     password_field = driver.find_element_by_id('username')
#     driver.quit()

    # def test_wait_for_visibility_1(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://the-internet.herokuapp.com/')
    #     self.driver.find_element_by_link_text('Dynamic Loading').click()
    #     self.driver.find_element_by_partial_link_text('Example 1').click()
    #     finish_messege = self.driver.find_element_by_id('finish')
    #     assert not finish_messege.is_displayed()
    #     start_button = self.driver.find_element_by_css_selector('#start button')
    #     start_button.click()
    #     wait = WebDriverWait(self.driver, 15)
    #     wait.until(lambda driver: not start_button.is_displayed())
    #     assert not start_button.is_displayed()
    #     wait.until(EC.visibility_of(finish_messege))
    #     assert finish_messege.is_displayed()
    #     self.driver.quit()
    # def is_present(self):


    def test_wait_for_visibility_2(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Dynamic Loading').click()
        self.driver.find_element_by_partial_link_text('Example 2').click()
        # finish_messege = self.driver.find_element_by_id('finish')
        # assert not finish_messege.is_enabled()
        try:
            len(self.driver.find_elements_by_id('finish')) >= 1
        except:
            pass
        start_button = self.driver.find_element_by_css_selector('#start button')
        start_button.click()
        wait = WebDriverWait(self.driver, 15)
        wait.until(lambda driver: not start_button.is_displayed())
        assert not start_button.is_displayed()
        while not self.driver.find_elements_by_id('finish'):
            try:
                self.driver.find_element_by_id('finish')
            except:
                continue
        # wait.until(EC.alert_is_present(self.driver.find_element_by_id('finish')))
        finish_messege = self.driver.find_element_by_id('finish')
        wait.until(EC.visibility_of(finish_messege))
        assert finish_messege.is_displayed()
        self.driver.quit()
