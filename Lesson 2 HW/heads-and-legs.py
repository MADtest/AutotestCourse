def animals(heads, legs):
    Chickens = 0
    Cows = 0
    if legs > 0 and heads > 0 and type(legs) == int and type(heads) == int and legs >= 2*heads and legs & 1 == 0:
        Cows = legs / 2 - heads
        Chickens = heads - Cows
        return (Chickens, Cows)
    else:
        return ("No solutions")

print animals(72, 200) #, (44, 28))
print animals(116, 282) #, (91, 25))
print animals(12, 24)#, (12, 0))
print animals(6, 24)#, (0, 6))
print animals(344, 872)##, (252, 92))
print animals(158, 616)# , (8, 150))

print animals(-370.0, 424.0)
