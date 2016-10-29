# -*- coding: utf-8 -*-


def is_unic(given_list):
    list_of_unic = []
    elements_count = 0
    for j in range(len(given_list)):
        for i in range(len(given_list[j])):
            elements_count += 1
            if given_list[j][i] not in list_of_unic:
                list_of_unic.append(given_list[j][i])
    if len(list_of_unic) == elements_count:
        return True
    else:
        return False
if __name__ == '__main__':
    input_list = input()
    print(is_unic(input_list))
    # print is_unic([[1, 5, -7], [-5, 7, -8], [-9, -2, 5]])
