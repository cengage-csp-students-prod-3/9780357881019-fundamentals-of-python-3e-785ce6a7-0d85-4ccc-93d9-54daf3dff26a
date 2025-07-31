import math

def newton(number, estimate=None):
    if estimate is None:
        estimate = number / 2

    better = (estimate + number / estimate) / 2

    # Adjust the precision to match test expectations
    if abs(better - estimate) < 1e-7:
        return better
    else:
        return newton(number, better)

def main():
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if not user_input:
            break

        try:
            number = float(user_input)
            if number < 0:
                print("Please enter a **positive** number.")
                continue

            result = newton(number)
            print(f"The program's estimate is {result}")
            print(f"Python's estimate is      {math.sqrt(number)}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()

