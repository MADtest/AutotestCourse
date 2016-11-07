# -*- coding: utf-8 -*-

import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Execution time for {} is %f".format(f.__name__) % (time.time()-t)
        return res
    return tmp


@timer
def factorial(x):
    r = 1
    for i in range(x):
        r *= (i+1)
    return r


def recf(n):
    if n == 0:
        return 1
    return recursion_factorial(n - 1) * n


@timer
def recursion_factorial(f):
    return f


@timer
def reduce_factorial(n):
    return reduce(lambda x, y: x*y, range(1, n-1))

if __name__ == '__main__':
    factorial(99999)
    recursion_factorial(recf(99999))
    reduce_factorial(99999)
