import math
def find_digit(num, nth):
    num1 = str(int(math.fabs(num)))
    nlist = list(num1)
    nlist.reverse()
    if nth <= 0:
        return -1
    elif nth <= len(nlist):
        return int(nlist[nth-1])
    else:
        return 0

print find_digit(5673, 4)
print find_digit(129, 2)
print find_digit(-2825, 3)
print find_digit(0, 20)
print find_digit(65, 0)
print find_digit(24, -8)
