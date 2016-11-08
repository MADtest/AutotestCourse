# -*- coding: utf-8 -*-


def args_and_result_or_error_to_file(f):
    def log_function(*args, **kwargs):
        with open('c:\ms\10.txt', 'a') as file:
            file.write(*args, **kwargs)
            try:
                if Exception:
                    with open('c:\ms\10.txt', 'a') as file:
                        file.write(Exception)
                else:
                    with open('c:\ms\10.txt', 'a') as file:
                        file.write(f(*args, **kwargs))
    return log_function

if __name__ == '__main__':
    pass
