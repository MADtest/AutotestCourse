import json

b = {1: 'Smith', 2: 'John', 3: 'Bob', 4: 'False, 5: None'}

if __name__ == '__main__':
    print json.loads('{"first name":"John", "last name":"Smith", "age":45}')

    print json.dump(b)
    print json.loads(b)

