# -*- coding: utf-8 -*-
from Lectures.framework.pages.login_page import login
from Lectures.framework.pages.home_page import logout
from Lectures.framework.dto import user
from Lectures.framework.locators import locator
from Lectures.framework.helpers.navigator import get
from Lectures.framework.assertions.custom_assert import assert_on_login_page, assert_on_home_page


def test_login():

    get(login)
    login((user.name, user.password))
    if assert_on_login_page():
        pass

    get(logout())
    if assert_on_home_page():
        pass


if __name__ == '__main__':
    test_login()
