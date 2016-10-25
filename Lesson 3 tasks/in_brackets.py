# -*- coding: utf-8 -*-

def in_brackets(input_string, replacement, all_or_not = 0):
    last_index = 0
    starts = [1]
    ends = [1]
    while last_index < len(ends):
        print last_index
        starts = []
        ends = []
        for i in range(len(input_string[last_index:])):
            if input_string[i] == '(':
                starts.append(i)
            elif input_string[i] == ')':
                ends.append(i)
        end_index = 0
        # last_index = 0

        for i in range(len(ends)):
            if ends[i] < starts[i+1]:
                end_index = i
                input_string = input_string.replace(input_string[starts[0] + 1:ends[end_index]], replacement)
                starts = []
                ends = []
                for j in range(len(input_string[last_index:])):
                    if input_string[j] == ')':
                        last_index = j+1
                        # print input_string[last_index:]
                        break
                break
    return input_string

if __name__ == '__main__':
    print in_brackets('dssvf (sdf(rb(jfgx)fdb)(sfsd)ski) fsdgsf (dsgds)mk ', 'RRRR')
