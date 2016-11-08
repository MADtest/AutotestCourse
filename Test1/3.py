# -*- coding: utf-8 -*-


def num_summ7():
    result_list = []
    i = 100
    while i < 1000:
        summ = 0
        for j in str(i):
            summ += int(j)
            if summ == 7:
                result_list.append(i)
        i += 1
    return  result_list

if __name__ == '__main__':
    num_summ7()