# -*- coding: utf-8 -*-


def args_check(func):
    def wrapper(string1, string2, brackets, variant):
        if type(string1) != str:
            print 'Parameter 1 is not a string.'
        elif type(string2) != str:
            print 'Parameter 2 is not a string.'
        elif brackets not in ('()', '{}', '[]'):
            print 'Parameter 3 is not brackets, valid options are () or {} or [].'
        elif variant not in (0, 1):
            print 'Parameter 4 is not 0 or 1.'
        else:
            res = func(string1, string2, brackets, variant)
            return res
    return wrapper

@args_check
def in_brackets(string1, string2, brackets, variant):
    print 'All args are correct'


if __name__ == '__main__':
    in_brackets('', '', '()', 0)
