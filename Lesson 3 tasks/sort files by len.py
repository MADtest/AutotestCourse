# -*- coding: utf-8 -*-
input_string = raw_input()

list_of_words = list(input_string.split(' '))
list_of_words.sort(key=len)
print list_of_words
