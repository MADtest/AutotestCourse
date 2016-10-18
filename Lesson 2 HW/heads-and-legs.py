def animals(heads, legs):
    Chickens = 0
    Cows = 0
    if legs >= 0 and heads >= 0 and type(legs) == int and type(heads) == int and legs >= 2*heads and legs & 1 == 0:
        Cows = legs / 2 - heads
        Chickens = heads - Cows
        if Chickens >= 0 and Cows >= 0:
            return (Chickens, Cows)
        else:
            return ("No solutions")
    else:
        return ("No solutions")
