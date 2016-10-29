# -*- coding: utf-8 -*-

list_of_unic = []
elements_count = 0


def is_unic(given_list):
    global elements_count, list_of_unic
    for j in range(len(given_list)):
        for i in range(len(given_list[j])):
            if type(given_list[j][i]) == list:
                is_unic(given_list[j])
            else:
                elements_count += 1
                if given_list[j][i] not in list_of_unic:
                    list_of_unic.append(given_list[j][i])
                else:
                    # print given_list[j][i], list_of_unic
                    return False
    if len(list_of_unic) == elements_count:
        return True
    else:
        return False
if __name__ == '__main__':
    input_list = input()
    print(is_unic(input_list))
    # print is_unic([[1, 5, -7], [-5, 7, -8], [-9, -2, 4]])
    # print is_unic([[27, 29, 2, 4, 13, 36], [9, 11, 20, 22, 31, 18], [32, 25, 7, 3, 21, 23], [14, 16, 34, 30, 12, 5],
    #                [28, 6, 15, 17, 26, 19], [1, 24, 33, 35, 8, 10]])
    # print(is_unic([[[i**j+k for j in range(4)] for i in range(4)]for k in range(4)]))
