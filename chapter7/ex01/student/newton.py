TOLERANCE = 0.000001

def recursive_newton(x, estimate):
    """Performs one Newton step recursively until the estimate matches expected precision."""
    new_estimate = (estimate + x / estimate) / 2
    if abs(new_estimate ** 2 - x) > TOLERANCE:
        return recursive_newton(x, new_estimate)
    else:
        return new_estimate

def newton(x, estimate=None):
    """Wrapper for Newton's method that starts with x / 2."""
    if estimate is None:
        estimate = x / 2
    return recursive_newton(x, estimate)

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

