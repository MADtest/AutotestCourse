# -*- coding: utf-8 -*-


def add_a_number_to_make_summ_of_elements_equal_zero(list):
    # needed = 0
    # for i in list:
    #     needed += i
    needed = sum(list)
    if needed > 0:
        while needed > 9:
            list.append(-9)
            needed += -9
        list.append(-1*needed)
    elif needed < 0:
        while needed < -9:
            list.append(9)
            needed += 9
        list.append(-1*needed)
    return list


def add_element_to_zero_sum(array):
    disbalance = sum(array)
    if disbalance:
        k, v = divmod(abs(disbalance), 9)
        sign = disbalance / abs(disbalance) * -1
        list_to_add = [9 * sign] * k
        if v:
            list_to_add.append(v * sign)

        array.extend(list_to_add)

    return array


if __name__ == '__main__':
    print(add_a_number_to_make_summ_of_elements_equal_zero([5, 7, -9, 8, -99, 56, 56, -88]))
    print(add_a_number_to_make_summ_of_elements_equal_zero([9, 9, 9, 9, 9, 9, 9, 9]))
    print(add_a_number_to_make_summ_of_elements_equal_zero([9, -9, 928]))
    print(add_a_number_to_make_summ_of_elements_equal_zero([1, 2, 3, -1, 0, 4]))
    print(add_element_to_zero_sum([1, 2, 3, -1, 0, 4]))