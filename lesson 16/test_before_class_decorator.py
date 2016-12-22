import pytest


# @pytest.fixture
#     def before():
#         print ('\nbefore each test')

@pytest.mark.usefixtures("before")
class TestClass:

    @pytest.fixture
    def before(self):
        print ('\nbefore each test')

    # @pytest.mark.usefixtures("before")
    def test_1(self):
        print('test 1()')

    # @pytest.mark.usefixtures("before")
    def test_2(self):
        print('test 2()')

    # @pytest.mark.usefixtures("before")
    def test_3(self):
        print('test 3()')
