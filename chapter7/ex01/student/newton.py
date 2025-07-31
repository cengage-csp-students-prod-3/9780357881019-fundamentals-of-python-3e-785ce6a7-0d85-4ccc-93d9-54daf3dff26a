def newton(n, estimate=None, tolerance=1e-7):
    if estimate is None:
        estimate = n / 2 if n >= 2 else 1

    better_estimate = 0.5 * (estimate + n / estimate)

    if abs(better_estimate - estimate) < tolerance:
        return better_estimate
    else:
        return newton(n, better_estimate, tolerance)

def main():
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if user_input == '':
            break
        try:
            num = float(user_input)
            if num <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a positive number.")
            continue

        estimate = newton(num)
        print(f"The program's estimate is {estimate}")
        import math
        print(f"Python's estimate is      {math.sqrt(num)}")

if __name__ == "__main__":
    main()
