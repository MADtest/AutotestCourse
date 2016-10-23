# -*- coding: utf-8 -*-

input_string = raw_input()

words = list(input_string.split(' '))

for i in range(len(words)):
    if words[i][0] in ('a', 'e', 'i', 'o', 'u'):
        words[i] += 'way'
    else:
        words[i] = words[i][1:] + words[i][0] + 'ay'

result_string = ''
for i in words:
    result_string += ' ' + i

print result_string
