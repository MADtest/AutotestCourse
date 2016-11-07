# -*- coding: utf-8 -*-


def wrapper(f):
    def replacement_function(*args, **kwargs):
        import time
        print 'Sleeping for 2 sec'
        time.sleep(2)
        return f(*args, **kwargs)
    return replacement_function


def wrapper(seconds):
    def replacement_function(*args, **kwargs):
        import time
        print 'Sleeping for {} seconds'.format(seconds)
        time.sleep(2)
        return f(*args, **kwargs)
    return replacement_function


def func(x, y):
    print x+y

func = wrapper(func)

func(1, 2)

