# -*- coding: utf-8 -*-


def logger(path='c:\ms\log-default.txt'):
    def wrapper(func):
        def replacement_function(*args, **kwargs):
            import time
            with open(path, 'a') as log_file:
                log_file.write('Function {} called at {}!!!\n'
                               .format(func.__name__, time.asctime()))
        return replacement_function
    return wrapper


@logger()
def summarize(x, y):
    return x+y


if __name__ == '__main__':
    print str(summarize(2, 3))

