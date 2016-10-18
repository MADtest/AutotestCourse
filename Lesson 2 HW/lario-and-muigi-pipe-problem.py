def pipe_fix(p):
    r = []
    for i in range(p[len(p) - 1] - p[0] + 1):
        r.append(p[0] + i)
    return r
