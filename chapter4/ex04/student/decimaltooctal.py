# decimaltooctal.py

def decimal_to_octal(decimal_number):
    if decimal_number == 0:
        return "0"
    octal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_number = str(remainder) + octal_number
        decimal_number //= 8
    return octal_number

# Main program
try:
    decimal_input = int(input("Enter a decimal integer: "))
    octal_result = decimal_to_octal(decimal_input)
    print(f"The octal representation is {octal_result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

