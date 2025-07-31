def expo(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * expo(base, exponent - 1)
