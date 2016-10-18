def pattern(n):
    r = '1'
    for i in range(n-1):
        r += '\n' + '1' + ('*'*(i+1))  + str(i+2)
    return r