def main():
    import math

    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if user_input == "":
            break

        x = float(user_input)
        result = newton(x)
        print(f"The program's estimate is {result}")
        print(f"Python's estimate is      {math.sqrt(x)}")

if __name__ == "__main__":
    main()
def limitReached(x, estimate):
    """Returns True if the current estimate is within the tolerance level."""
    return abs(estimate ** 2 - x) <= TOLERANCE
def improveEstimate(x, estimate):
    """Improves the current estimate using Newton's method."""
    return (estimate + x / estimate) / 2
def newton(x):
    """Returns the square root of x using Newton's method."""
    estimate = x / 2
    while not limitReached(x, estimate):
        estimate = improveEstimate(x, estimate)
    return estimate
