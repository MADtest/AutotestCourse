def no_boring_zeros(n):
    n = str(n)
    if len(n) > 1:
        while n[-1] == '0':
            n = n[:-1]
    return int(n)