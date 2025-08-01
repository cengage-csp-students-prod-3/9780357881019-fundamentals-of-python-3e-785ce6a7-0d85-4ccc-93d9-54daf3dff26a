def newton(n, estimate=None, count=0, max_iterations=6):
    if estimate is None:
        estimate = n / 2 if n >= 2 else 1

    if count >= max_iterations:
        return estimate

    better_estimate = 0.5 * (estimate + n / estimate)
    return newton(n, better_estimate, count + 1, max_iterations)

# Test cases:
for num in [2, 4, 9]:
    result = newton(num)
    print(f"newton({num}) = {result:.16f}")


if __name__ == "__main__":
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if user_input == '':
            break
        try:
            number = float(user_input)
            if number <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a positive number.")
            continue

        estimate = newton(number)
        print(f"The program's estimate is {estimate}")
        import math
        print(f"Python's estimate is      {math.sqrt(number)}")
