# octaltodecimal.py

def octal_to_decimal(octal_string):
    decimal_number = 0
    for index, digit in enumerate(reversed(octal_string)):
        if digit not in '01234567':
            raise ValueError("Invalid octal digit detected.")
        decimal_number += int(digit) * (8 ** index)
    return decimal_number

# Main program
try:
    octal_input = input("Enter a string of octal digits: ")
    decimal_result = octal_to_decimal(octal_input)
    print(f"The integer value is {decimal_result}")
except ValueError as e:
    print(f"Error: {e}")
