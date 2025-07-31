TOLERANCE = 0.000001

def newton(x, estimate=None):
    """Recursively approximates the square root of x with controlled precision."""
    if estimate is None:
        estimate = x / 2  # initial guess

    improved = (estimate + x / estimate) / 2
    if abs(improved ** 2 - x) <= TOLERANCE:
        return improved
    else:
        return newton(x, improved)


def main():
    import math

    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if user_input == "":
            break
        x = float(user_input)
        result = newton(x)
        print("The program's estimate is", result)
        print("Python's estimate is     ", math.sqrt(x))


if __name__ == "__main__":
    main()

