# -*- coding: utf-8 -*-
import sys
max_element = -sys.maxint


def find_max_element_in_a_matrix(input_list):
    global max_element
    for i in range(len(input_list)):
        if type(input_list[i]) == type(list):
            find_max_element_in_a_matrix(input_list[i])
        else:
            if input_list[i] > max_element:
                max_element = input_list[i]
    return max_element

if __name__ == '__main__':
    print find_max_element_in_a_matrix([[1, 2, 3], [4, 11, 6], [7, 8, 9]])

