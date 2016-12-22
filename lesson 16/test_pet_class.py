import requests
import json
import pytest


class Pet:

    def test_pet_adding(self):
        self.data = {
              "id": 0,
              "username": "msUser",
              "firstName": "First",
              "lastName": "Last",
              "email": "fl@mymail.corp",
              "password": "qwerty",
              "phone": "123",
              "userStatus": 0
            }
        self.header = {'Authorization'}
        self.baseUrl = 'http://petstore.swagger.io/v2/pet/13'
        self.method = ''
        requests.post(self.baseUrl, headers=self.header, data=json.dumps(self.data))


if __name__ == '__main__':
    print Pet.test_pet_adding
    print requests.get('http://petstore.swagger.io/v2/pet/13').json()

