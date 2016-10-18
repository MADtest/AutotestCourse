x = input("What number of fibanacci's list a you interested in?\n")
fibanacci = [0, 1]
for i in range(x+1):
    if i > 1:
        fibanacci.append(fibanacci[i-1] + fibanacci[i-2])
print fibanacci[-1]

