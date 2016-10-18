def iq_test(numbers):
    o = []
    e = []
    for i in numbers:
        if int(i) & 1:
            o.append(i)
        else:
            e.append(i)
    if len(o) == 1:
        return o[0]
    elif len(e) == 1:
        return e[0]
    print(o, e)
iq_test([2, 4, 7, 8, 10])

