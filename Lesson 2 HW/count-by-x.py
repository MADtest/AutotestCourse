def count_by(x, n):
    r = []
    for i in range(n):
        r.append(x*(i+1))
    return r

print count_by(50, 5)