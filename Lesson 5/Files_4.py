# -*- coding: utf-8 -*-


def sorter(path1, path2):
    with open(path1, 'r') as file1:
        for line in file1:
            with open(path2, 'a') as file2:
                file2.write(line)


if __name__ == '__main__':
    sorter('c:\ms\License_BY.txt', 'c:\ms\License_BY_output.txt')
