# -*- coding: utf-8 -*-


def add_a_number_to_make_summ_of_elements_equal_zero(list):
    needed = 0
    for i in list:
        needed += i
    list.append(-1*needed)
    return list

if __name__ == '__main__':
    print(add_a_number_to_make_summ_of_elements_equal_zero([5, 7, -9, 8, -99, 56, 56]))
