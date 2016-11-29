# -*- coding: utf-8 -*-


def get_numbers_from_an_integer():
    result_list = []
    for i in range(100, 1000):
        first_digit, second_digit, third_digit = i // 100, (i % 100) // 10, i % 10
        if first_digit + second_digit + third_digit == 7:
            result_list.append(i)
    return result_list


if __name__ == '__main__':
    print get_numbers_from_an_integer()

