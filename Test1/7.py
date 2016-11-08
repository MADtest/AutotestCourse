# -*- coding: utf-8 -*-


def reversed_matrix(list):
    result_list = []
    for i in range(len(list)):
        result_list.append([])
        for j in range(len(list)):
            result_list[i].append(list[j][i])
    return result_list

if __name__ == '__main__':
    print reversed_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

