# -*- coding: utf-8 -*-


def print_a_file(path):
    try:
        with open(path, 'r') as file:
            print file.read()
    except EnvironmentError:
        print 'Something went wrong!'


if __name__ == '__main__':
    print_a_file('c:\ms\log.txt')
