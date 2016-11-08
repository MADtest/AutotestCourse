# -*- coding: utf-8 -*-


def calculate_nedded_lines(path, line):
    lines = 0
    with open(path) as input_file:
        for i in input_file.readlines():
            if i == line:
                lines += 1
    return lines

if __name__ == '__main__':
    print calculate_nedded_lines('c:\ms\License_BY_output.txt', '2. Правы і абавязкі Бакоў\n')
