def positive_sum(arr):
    n = 0
    for i in arr:
        if i > 0:
            n += i
    return n