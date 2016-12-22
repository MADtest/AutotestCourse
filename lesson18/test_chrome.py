from selenium import webdriver

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get('http://tut.by')
    driver.refresh()
    driver.back()
    driver.forward()
    driver.get('https://the-internet.herokuapp.com/')
    links = driver.find_elements_by_css_selector('a')
    # len(links)
    target_link = filter(lambda x: 'Form Authentication' in x.text, links)
    # len(target_link)
    target_link[0].click()
    assert 'login' in driver.current_url
    driver.close()
