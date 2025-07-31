def newton(number, estimate=None):
    if number == 0:
        return 0  # edge case: square root of 0 is 0

    if estimate is None:
        estimate = number / 2  # initial estimate

    # Compute a better estimate
    better = (estimate + number / estimate) / 2

    # Check if the estimate is "good enough"
    if abs(better - estimate) < 1e-10:
        return better
    else:
        return newton(number, better)
import math

def main():
    while True:
        entry = input("Enter a positive number or enter/return to quit: ")
        if not entry:
            break

        number = float(entry)
        estimate = newton(number)

        print("The program's estimate is", estimate)
        print("Python's estimate is     ", math.sqrt(number))

if __name__ == "__main__":
    main()
