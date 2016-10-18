x = input('Enter a number:\n')
summ = 0
multi = 1
for i in list(str(x)):
    summ += int(i)
    multi *= int(i)
print (summ, multi)
