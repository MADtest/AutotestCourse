import csv, json, yaml
from yaml import dump,load, load_all


class Book(object):
    def __init__(self, name=None, author=None, isbn=None):
        self.name = name
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return 'Book: name - "{name}", author - {author}, isbn - {isbn}'\
            .format(name=self.name, author=self.author, isbn=self.isbn)


class Library(object):
    def __init__(self):
        pass

    def add(self):
        print 'Enter new book name, author and isbn:'
        self.book_name =



if __name__ == '__main__':
    b1 = Book('iBook', 'Bob Dylan', 1234567890)
    print b1
    dump(b1, open('lib_yaml.yaml', 'w'), default_flow_style=False)
