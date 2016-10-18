def fuelPrice(litres, pricePerLiter):
    n = 0.05 * int(litres/2)
    if litres >= 2:
        if n <= 0.25:
            return round((litres * (pricePerLiter - n)), 2)
        elif n > 0.25:
            return round((litres * (pricePerLiter - 0.25)), 2)
    else:
        return round((litres * pricePerLiter), 2)


