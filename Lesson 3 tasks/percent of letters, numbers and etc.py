import string

input_string = raw_input()
letters = 0
numbers = 0
symbols = 0

print input_string
for i in range(len(input_string)):
    if input_string[i] in string.ascii_lowercase:
        letters += 1
    elif input_string[i] in string.digits:
        numbers += 1
    else:
        symbols += 1
print (letters, numbers, symbols)

