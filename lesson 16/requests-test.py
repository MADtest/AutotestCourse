import requests, json

# def test_create_pet():
#     data = {}
#     header = {}
#     baseUrl = ''
#     method = ''
#     requests.post(url, headers=header, data=json.dumps(data))



if __name__ == '__main__':
    response = requests.get('http://petstore.swagger.io/v2/pet/13')
    print response.status_code
    print response.ok
    print response.json()
    assert response.status_code == 200
    # assert response.json()['name'] == 'doggie'

