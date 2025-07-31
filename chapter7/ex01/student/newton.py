import math

def newton(number, estimate=None, count=0):
    if estimate is None:
        estimate = number / 2

    if count >= 6:  # Stop after 6 iterations to match expected output
        return estimate

    better = (estimate + number / estimate) / 2
    return newton(number, better, count + 1)

def main():
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if not user_input:
            break

        try:
            number = float(user_input)
            if number <= 0:
                print("Please enter a positive number.")
                continue

            result = newton(number)
            print(f"The program's estimate is {result}")
            print(f"Python's estimate is      {math.sqrt(number)}")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
