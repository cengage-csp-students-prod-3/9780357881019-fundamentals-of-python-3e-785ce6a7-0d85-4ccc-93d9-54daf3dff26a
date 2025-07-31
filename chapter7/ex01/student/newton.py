num = float(input("Enter a positive number or enter/return to quit: "))
if num > 0:
    estimate = newton(num)
    print(f"The program's estimate is {estimate}")
    import math
    print(f"Python's estimate is      {math.sqrt(num)}")


