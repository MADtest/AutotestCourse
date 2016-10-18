def super_size(n):
    l = []
    for i in sorted(list(str(n))):
        l.append(i)
    return int(''.join(map(str, reversed(l))))
