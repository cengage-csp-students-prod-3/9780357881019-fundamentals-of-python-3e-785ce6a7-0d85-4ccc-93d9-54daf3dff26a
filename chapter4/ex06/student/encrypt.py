# encrypt.py

def decimal_to_binary(n):
    """Manually converts a decimal number to a binary string."""
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def encrypt_message(message):
    encrypted_list = []

    for char in message:
        ascii_plus_1 = ord(char) + 1                   # Step 1
        binary_str = decimal_to_binary(ascii_plus_1)   # Step 2
        shifted = binary_str[1:] + '0' if len(binary_str) > 1 else '0'  # Step 3
        encrypted_list.append(shifted)

    return ' '.join(encrypted_list)                    # Step 4


# Main program
if __name__ == "__main__":
    user_input = input("Enter a message: ")
    print(encrypt_message(user_input))
