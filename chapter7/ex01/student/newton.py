TOLERANCE = 0.000001

def newton(x, estimate=None):
    """Recursively approximates the square root of x."""
    if estimate is None:
        estimate = x / 2  # initial guess

    if abs(estimate ** 2 - x) <= TOLERANCE:
        return estimate
    else:
        # improve the estimate and recurse
        new_estimate = (estimate + x / estimate) / 2
        return newton(x, new_estimate)


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
