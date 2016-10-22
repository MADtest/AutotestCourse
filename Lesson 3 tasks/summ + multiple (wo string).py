x = input('Enter a number:\n')
summ = 0
multi = 1
list_of_numbers = []

razryad = 1
razryad_range = 0

while x/razryad >= 1:
    razryad *= 10
    razryad_range += 1

for i in range(razryad_range):
    list_of_numbers.append(int(x/(((10**(razryad_range-(i+1)))))))
    summ += list_of_numbers[i]
    multi *= list_of_numbers[i]
    x -= list_of_numbers[i]*(10**(razryad_range-(i+1)))
print (summ, multi)
