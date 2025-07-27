# octal_decimal_converter.py

def decimal_to_octal(decimal_number):
    return format(decimal_number, 'o')  # built-in conversion

def octal_to_decimal(octal_string):
    return int(octal_string, 8)  # interpret input as base 8

def main():
    print("Octal ↔ Decimal Converter")
    print("1. Decimal to Octal")
    print("2. Octal to Decimal")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        try:
            decimal_input = int(input("Enter a decimal integer: "))
            print(decimal_to_octal(decimal_input))
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")
    elif choice == "2":
        try:
            octal_input = input("Enter a string of octal digits: ")
            print(octal_to_decimal(octal_input))
        except ValueError:
            print("Invalid input. Please enter valid octal digits (0-7).")
    else:
        print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
