import requests
import json


class Test_user:

    def test_create_user(self):
        self.data = {
                "id": 13,
                "username": "TestNickName",
                "firstName": "TestFirstName",
                "lastName": "TestLastName",
                "email": "test@test.test",
                "password": "PASSWORD",
                "phone": "03",
                "userStatus": 0
            }
        self.response = requests.get('http://petstore.swagger.io/v2/user/13')
        # self.header = {'Authorization'}
        self.baseUrl = 'http://petstore.swagger.io/v2/user/'
        # self.method = ''  headers=self.header,
        requests.post(self.baseUrl, data=json.dumps(self.data))

        return self.response.json()

if __name__ == '__main__':
    print Test_user.test_create_user()
    print requests.get('http://petstore.swagger.io/v2/user/13')