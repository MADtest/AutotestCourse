def digitize(n):
    l = []
    for i in reversed(list(str(n))):
        l.append(int(i))
    return l

