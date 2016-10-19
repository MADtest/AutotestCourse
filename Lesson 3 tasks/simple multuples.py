x = input("Enter a number\n")
ListOfSimples = []
ListOfSimplesDevides = []
for j in range(x):
    for i in range(j):
        if i > 1:
            if j % i == 0:
                break
            elif i == j-1 and j % i == 1:
                ListOfSimples.append(j)
while x != 1:
    for i in range(len(ListOfSimples)):
        if x % ListOfSimples[-i-1] == 0:
            ListOfSimplesDevides.append(ListOfSimples[-i-1])
            x = x / ListOfSimples[-i-1]
            continue
        else:
            continue
print max(ListOfSimplesDevides)
