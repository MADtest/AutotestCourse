# -*- coding: utf-8 -*-
import inspect


def args_and_result_or_error_to_file(f):
    def log_function(*args, **kwargs):
        with open('c:\ms\log10.txt', 'a') as file:
            file.write(str(inspect.getargspec(f))+'\n')
            # file.write(str(*args) + ' ' + str(**kwargs))
        try:
            f(*args, **kwargs)
        except Exception as e:
            with open('c:\ms\log10.txt', 'a') as file:
                file.write(str(e)+'\n')
        else:
            with open('c:\ms\log10.txt', 'a') as file:
                file.write(str(f(*args, **kwargs))+'\n')

    return log_function


@args_and_result_or_error_to_file
def any_func(x, y):
    return x - y

if __name__ == '__main__':
    any_func('asd', 'fsad', 'age', 1243, ['adsf', ''])
    any_func(5, 8)

