# octal_decimal_converter.py

def decimal_to_octal(decimal_number):
    if decimal_number == 0:
        return "0"
    octal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_number = str(remainder) + octal_number
        decimal_number //= 8
    return octal_number

def octal_to_decimal(octal_string):
    decimal_number = 0
    exponent = 0
    for digit in reversed(octal_string):
        if digit not in '01234567':
            raise ValueError("Invalid octal digit.")
        decimal_number += int(digit) * (8 ** exponent)
        exponent += 1
    return decimal_number

def main():
    print("Octal ↔ Decimal Converter")
    print("1. Decimal to Octal")
    print("2. Octal to Decimal")
    
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        try:
            decimal_input = int(input("Enter a decimal integer: "))
            octal_output = decimal_to_octal(decimal_input)
            print(f"The octal representation is {octal_output}")
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")
    elif choice == "2":
        octal_input = input("Enter a string of octal digits: ")
        try:
            decimal_output = octal_to_decimal(octal_input)
            print(f"The integer value is {decimal_output}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
