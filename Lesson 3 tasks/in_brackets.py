# -*- coding: utf-8 -*-

def in_brackets(input_string, replacement, all_or_not = 0):
    starts = []
    ends = []
    for i in range(len(input_string)):
        if input_string[i] == '(':
            starts.append(i)
        elif input_string[i] == ')':
            ends.append(i)
    end_index = 0
    for i in range(len(ends)):
        if ends[i] < starts[i+1]:
            end_index = i
            break
    return input_string.replace(input_string[starts[0]+1:ends[end_index]], replacement)

if __name__ == '__main__':
    print in_brackets('dssvf (sdf(rb(jfgx)fdb)(sfsd)ski) fsdgsf (dsgds) ', 'RRRR')
