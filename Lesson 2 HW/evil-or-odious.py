def evil(n):
    r = 0
    for i in bin(n)[2:]:
        if i == '1':
            r += 1
    if r & 1:
        return "It's Odious!"
    else:
        return "It's Evil!"
