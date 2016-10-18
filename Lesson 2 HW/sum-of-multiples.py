def sum_mul(n, m):
    if type(n) == int and type(m) == int and n > 0 and m > 0:
        r = 0
        for i in range(m-1):
            if (i+1) % n == 0:
                r += (i + 1)
        return r
    else:
        return 'INVALID'


