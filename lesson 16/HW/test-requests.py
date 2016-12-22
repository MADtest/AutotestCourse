import requests
import json
# import pytest


# class Test_user:
#
#     def test_create_user(self):
#         self.data = {
#                 "id": 13,
#                 "username": "TestNickName",
#                 "firstName": "TestFirstName",
#                 "lastName": "TestLastName",
#                 "email": "test@test.test",
#                 "password": "PASSWORD",
#                 "phone": "03",
#                 "userStatus": 0
#             }
#         self.baseUrl = 'http://petstore.swagger.io/v2/user/'
#         requests.post(self.baseUrl, data=json.dumps(self.data))
#         assert requests.post(self.baseUrl, data=json.dumps(self.data)).status_code == 200
#
#     def test_user_login(self):
#         self.baseUrl = 'http://petstore.swagger.io/v2/user/login'
#         requests.get(self.baseUrl, username='TestNickName', password='PASSWORD')
#         assert requests.get(self.baseUrl, username='TestNickName', password='PASSWORD').status_code == 0
#
#     def test_get_user(self):
#         self.baseUrl = 'http://petstore.swagger.io/v2/user/TestNickName'
#         requests.get(self.baseUrl)
#         assert requests.get(self.baseUrl).status_code == 200
#         return requests.get(self.baseUrl)
#
#
#     def test_user_logout(self):
#         self.baseUrl = 'http://petstore.swagger.io/v2/user/logout'
#         requests.get(self.baseUrl)
#         assert requests.get(self.baseUrl).status_code == 200

if __name__ == '__main__':
    data = {
        "id": 13,
        "username": "TestNickName",
        "firstName": "TestFirstName",
        "lastName": "TestLastName",
        "email": "test@test.test",
        "password": "PASSWORD",
        "phone": "03",
        "userStatus": 0
    }
    baseUrl = 'http://petstore.swagger.io/v2/user/'
    response = requests.post(baseUrl, data=json.dumps(data))
    print response.status_code == 200
    # print response.json()


    baseUrl = 'http://petstore.swagger.io/v2/user/TestNickName'
    info = requests.get(baseUrl)
    print info.status_code == 200
    print info.json()

    baseUrl = 'http://petstore.swagger.io/v2/user/login'
    login = requests.get(baseUrl, username='TestNickName', password='PASSWORD')
    print login.status_code == 0

    # baseUrl = 'http://petstore.swagger.io/v2/user/logout'
    # logout = requests.get(baseUrl)
    # print logout.status_code == 200
