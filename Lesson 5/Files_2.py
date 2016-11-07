# -*- coding: utf-8 -*-


def fibanacci_to_file(number, path):
    fibonacci = [0, 1]
    for i in range(number+1):
        if i > 1:
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    with open(path, 'wb') as result_file:
        for i in fibonacci:
             result_file.write(str(i)+', ')


if __name__ == '__main__':
    fibanacci_to_file(10, 'c:\ms\output_fibonacci.txt')
