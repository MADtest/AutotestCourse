# -*- coding: utf-8 -*-
# NOT FINISHED


def in_brackets(input_string, replacement, all_or_not='a'):
    is_end = 1
    start = 0
    end = 0
    result_string = ''

    if all_or_not == 'a':
        for i in range(len(input_string[start:])):
            if input_string[i] == '(':
                start = i
                while is_end != 0:
                    for j in range(len(input_string[start + 1:])):
                        if input_string[start + 1 + j] == '(':
                            is_end += 1
                        elif input_string[start + 1 + j] == ')':
                            is_end -= 1
                        elif is_end == 0:
                            result_string += input_string[end:start]
                            end = start + j + 1
                            break
        result_string += '(' + replacement + ')'

        # print input_string
        return result_string + input_string[end:]
    if all_or_not == 'b':
        while '(' in input_string[end:]:
        # if '(' in input_string[end:]:
            print end, input_string[end:]
            is_end = 1
            for i in range(len(input_string[end:])):
                kkk = len(input_string[end:])
                print result_string
                print end, i, end+i, len(input_string), range(len(input_string[end:])), input_string[end+i-1]

                if input_string[end + i - 1] == '(':
                    start = end + i - 1
                    while is_end != 0:
                        for j in range(len(input_string[start + 1:])):
                            if input_string[start + 1 + j] == '(':
                                is_end += 1
                            elif input_string[start + 1 + j] == ')':
                                is_end -= 1
                            elif is_end == 0:
                                result_string += input_string[end:start+1]
                                end = start + j + 1
                                # is_end = 1
                                break
            result_string += '(' + replacement + ')'

        return result_string
    # if all_or_not == 'b':
    #     while '(' in input_string[end:]:
    #         print input_string[end:]
    #         in_brackets(input_string[end:], replacement, 'a')
    #     return result_string
if __name__ == '__main__':

    # print in_brackets('dssvf (sd()f(rb(jfgx)fdb)(sfsd)ski) fsdgsf (ds(g)ds) sdf (ds(g)ds) sdf ', 'RRRR', 'a')
    print in_brackets('dssvf (sd()f(rb(jfgx)fdb)(sfsd)ski) fsdgsf (ds(g)ds) sdf (ds(g)ds) sdf J', 'RRRR', 'b')
