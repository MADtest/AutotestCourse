# -*- coding: utf-8 -*-


def is_string_polindrom(string):
    reverced_string = ''
    for i in range(len(string)):
        reverced_string += string[-i-1]
    if string == reverced_string:
        return True
    else:
        return False


if __name__ == '__main__':
    print is_string_polindrom('asdfgfdsa')

