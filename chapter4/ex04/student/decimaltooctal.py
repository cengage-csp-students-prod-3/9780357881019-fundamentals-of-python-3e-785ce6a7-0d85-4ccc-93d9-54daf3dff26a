# octal_decimal_converter.py

import sys

# Read the input from stdin
user_input = input().strip()

# Try to convert the input assuming it's an octal number
# and output the decimal equivalent.
try:
    print(int(user_input, 8))
except ValueError:
    # If it's not a valid octal number, assume it's a decimal
    # and output the octal equivalent.
    try:
        decimal_number = int(user_input)
        print(format(decimal_number, 'o'))
    except ValueError:
        print("Invalid input")
