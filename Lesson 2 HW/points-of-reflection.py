def symmetric_point(p, q):
    p1 = [0, 0]
    if p[0] > q[0]:
        p1[0] = q[0] - (p[0] - q[0])
    else:
        p1[0] = q[0] + (q[0] - p[0])
    if p[1] > q[1]:
        p1[1] = q[1] - (p[1] - q[1])
    else:
        p1[1] = q[1] + (q[1] - p[1])
    return p1
