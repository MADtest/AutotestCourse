# -*- coding: utf-8 -*-


def change_last(given_list):
    for i in range(len(given_list)):
        given_list[i][-1] = sum(given_list[i][:-1])
    return given_list
if __name__ == '__main__':
    input_list = input()
    print(change_last(input_list))
    # print change_last([[1, 5, -7], [-5, 7, -8], [-9, -2, 5]])
