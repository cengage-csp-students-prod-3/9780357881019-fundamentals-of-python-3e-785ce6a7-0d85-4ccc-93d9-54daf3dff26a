# Lookup table (dictionary) for digit-to-value mapping
DIGIT_TABLE = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13,
    'E': 14, 'F': 15
}

def repToDecimal(rep, base):
    """Converts a string representation of a number in a given base to decimal (base 10)."""
    rep = rep.upper()
    decimal_value = 0
    power = len(rep) - 1

    for digit in rep:
        value = DIGIT_TABLE[digit]
        decimal_value += value * (base ** power)
        power -= 1

    return decimal_value

def main():
    print("repToDecimal('10', 2)  =", repToDecimal("10", 2))   # 2
    print("repToDecimal('10', 8)  =", repToDecimal("10", 8))   # 8
    print("repToDecimal('10', 10) =", repToDecimal("10", 10))  # 10
    print("repToDecimal('10', 16) =", repToDecimal("10", 16))  # 16
    print("repToDecimal('1A', 16) =", repToDecimal("1A", 16))  # 26
    print("repToDecimal('F', 16)  =", repToDecimal("F", 16))   # 15
    print("repToDecimal('101', 2) =", repToDecimal("101", 2))  # 5

if __name__ == "__main__":
    main()
