import pytest


@pytest.fixture
def before():
    print ('\nbefore each test')


def test_1(before):
    print('test 1()')


def test_2(before):
    print('test 2()')

@pytest.mark.usefixtures("before")
def test_3():
    print('test 3()')

