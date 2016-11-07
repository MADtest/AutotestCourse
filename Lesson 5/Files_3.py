# -*- coding: utf-8 -*-


def sorter(path):
    with open(path, 'r') as file:
        alllines = []
        for line in file:
            alllines.append(line)
    alllines.sort(key=len)
    with open(path, 'a') as file1:
        for i in alllines:
            file1.write(i)


if __name__ == '__main__':
    sorter('c:\ms\License_BY.txt')
