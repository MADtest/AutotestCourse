# -*- coding: utf-8 -*-


def is_magic(given_list):
    n = len(given_list)
    m = (n*(n**2+1))/2
    column_sum = 0
    diagonal_1 = 0
    diagonal_2 = 0
    for i in range(n):
        if sum(given_list[i]) != m:
            return False
    for i in range(n):
        for j in range(n):
            column_sum += given_list[j][i]
        if column_sum != m:
            return False
        else:
            column_sum = 0
            continue
    for i in range(n):
        diagonal_1 += given_list[i][i]
        diagonal_2 += given_list[-i-1][-i-1]
    if diagonal_1 == m and diagonal_2 == m:
        return True #'The square is magic!'
    else:
        return False
if __name__ == '__main__':
    input_list = input()
    print(is_magic(input_list))
    # print is_magic([[1, 5, -7], [-5, 7, -8], [-9, -2, 5]])
    # print is_magic([[27,29,2, 4, 13, 36], [9, 11, 20, 22, 31, 18], [32, 25, 7, 3, 21, 23], [14, 16, 34, 30, 12, 5], [28, 6, 15, 17, 26, 19], [1, 24, 33, 35, 8, 10]])