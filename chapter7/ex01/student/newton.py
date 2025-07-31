TOLERANCE = 0.000001

def newton(x, estimate=None):
    """Recursive Newton's method exactly mimicking the iterative loop's output."""
    if estimate is None:
        estimate = x / 2

    next_estimate = (estimate + x / estimate) / 2

    if abs(next_estimate ** 2 - x) > TOLERANCE:
        return newton(x, next_estimate)
    else:
        return next_estimate  # Return only when the next one satisfies tolerance

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

