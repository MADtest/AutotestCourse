# -*- coding: utf-8 -*-


def in_brackets(input_string, replacement, all_or_not='a'):
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
    if all_or_not == 'a':
        return input_string.replace(input_string[starts[0]:ends[end_index]]+')', '('+replacement+')')
    if all_or_not == 'b':
        allstarts = [starts[0]]
        allends = [ends[end_index]]
        while allends[-1] < ends[-1]:
            # print starts, allstarts
            # print ends, allends
            for i in range(len(input_string[ends[end_index]:])):
                if input_string[ends[end_index] + i] == '(':
                    allstarts.append(ends[end_index] + i)
                    break
            for i in range(len(ends[end_index+1:])):
                # print end_index + i+2, len(starts)
                if end_index + i+2 <= len(starts):
                    if ends[end_index + i] < starts[end_index + i+1]:
                        allends.append(ends[end_index + i + 2])
                        end_index += i + 1
                        # print input_string[ends[end_index]]
                        break
                elif end_index + i+2 > len(starts):
                    allends.append(ends[end_index])
                    end_index += i
                    break
        # print allstarts, allends
        result_string = input_string
        for i in range(len(allstarts)):
            result_string = result_string.replace(input_string[allstarts[i]:allends[i]]+')', '('+replacement+')')
            # print '('+input_string[allstarts[i]:allends[i]]+')'
        # for i in allstarts:
        #     input_string.replace(input_string[allstarts[i]:allends[i]], replacement)
        return result_string

#
if __name__ == '__main__':

    print in_brackets('dssvf (sd()f(rb(jfgx)fdb)(sfsd)ski) fsdgsf (ds(g)ds) sdf (ds(g)ds) sdf ', 'RRRR', 'b')

