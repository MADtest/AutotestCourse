input_string = raw_input()

list_of_words = list(input_string.split(' '))
list_of_words.sort(key=len)
print len(list_of_words[0])
