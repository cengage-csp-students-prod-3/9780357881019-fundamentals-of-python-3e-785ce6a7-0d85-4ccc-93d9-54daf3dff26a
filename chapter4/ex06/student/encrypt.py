# encrypt.py

def encrypt_message(message):
    encrypted_bits = []

    for char in message:
        ascii_val = ord(char) + 1              # Step 1: Add 1 to ASCII
        binary_str = format(ascii_val, '08b')  # Step 2: Convert to 8-bit binary string
        shifted = binary_str[1:] + '0'         # Step 3: Shift left by 1 (bitwise)
        encrypted_bits.append(shifted)

    return ' '.join(encrypted_bits)            # Step 4: Join with space


# Main program
if __name__ == "__main__":
    user_input = input("Enter a message: ")
    result = encrypt_message(user_input)
    print(result)
