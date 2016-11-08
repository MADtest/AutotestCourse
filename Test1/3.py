# -*- coding: utf-8 -*-
result_list = []


def num_summ7():

    i = 100
    while i < 1000:
        summ = 0
        for j in str(i):
            summ += int(j)
            if summ == 7:
                result_list.append(i)
        i += 1


if __name__ == '__main__':
    num_summ7()
    print result_list