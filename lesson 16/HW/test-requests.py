import requests
import json
import pytest


@pytest.fixture
def user_data():
    baseUrl = 'http://petstore.swagger.io/v2'
    header = {'Content-type': 'application/json'}
    data = {
            "id": 13,
            "username": "TestNickName",
            "firstName": "TestFirstName",
            "lastName": "TestLastName",
            "email": "test@test.test",
            "password": "PASSWORD",
            "phone": "103",
            "userStatus": 1
        }
    return [baseUrl, header, data]


class TestRequests(object):
    def test_user_create(self, user_data):
        method = '/user'
        response = requests.post(user_data[0] + method, headers=user_data[1], data=json.dumps(user_data[2]))
        assert response.status_code == 200

    def test_user_login(self, user_data):
        method = '/user/login'
        response = requests.get(user_data[0] + method, auth=(user_data[2]['username'], user_data[2]['password']))
        assert response.status_code == 200, "Unexpected response code {0}.".format(response.status_code)
        assert response.content.find('logged in user session') != -1, "Unexpected response content."

    def test_user_get(self, user_data):
        method = '/user/' + user_data[2]['username']
        response = requests.get(user_data[0] + method)
        assert response.status_code != 400, 'Invalid username supplied'
        assert response.status_code != 404, 'User not found'
        assert response.status_code == 200, "Unexpected response code {0}.".format(response.status_code)
        assert dict(json.loads(response.content)) == user_data[2], 'User data is inconsistent'

    def test_user_update(self, user_data):
        user_data[2]['lastName'] = 'Married'
        method = '/user/' + user_data[2]['username']
        response = requests.put(user_data[0] + method, headers=user_data[1], data=json.dumps(user_data[2]))
        assert response.status_code != 400, 'Invalid username supplied'
        assert response.status_code != 404, 'User not found'
        assert response.status_code == 200, "Unexpected response code {0}.".format(response.status_code)

    def test_user_logout(self, user_data):
        method = '/user/logout'
        response = requests.get(user_data[0] + method)
        assert response.status_code == 200, "Unexpected response code {0}.".format(response.status_code)
        assert not response.content, "Response body is not empty."

    def test_user_delete(self, user_data):
        method = '/user/' + user_data[2]['username']
        response = requests.delete(user_data[0] + method)
        assert response.status_code != 400, 'Invalid username supplied'
        assert response.status_code != 404, 'User not found'
        assert response.status_code == 200, "Unexpected response code {0}.".format(response.status_code)
        assert not response.content, "Response body is not empty."

