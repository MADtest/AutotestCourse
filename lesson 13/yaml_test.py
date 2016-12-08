import yaml
from yaml import dump,load, load_all
data = ['2,True', '3,True', '12,False', '13,True']

if __name__ == '__main__':
    for i in load(open('person.yaml', 'r')):
        print i
    print load_all(open('person.yaml', 'r'))
    # load('''first name: John
    #         last name: Smith
    #         age: 45''')
    dump(data[0], open('person_output.yaml', 'w'))