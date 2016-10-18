x = input()
for i in range(x):
    if i > 1:
        if x % i == 0:
            print 'False'
            break
        elif i == x-1 and x % i == 1:
            print "True"

# print [x for x in range(x+1) if x & [1:x] == 0]