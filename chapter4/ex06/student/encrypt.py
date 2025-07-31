# encrypt.py

def encrypt_message(message):
    encrypted_list = []

    for char in message:
        ascii_val = ord(char) + 1                 # Step 1: Add 1 to ASCII value
        shifted_val = (ascii_val << 1) & 0xFF     # Step 2: Shift left by 1 bit, keep 8 bits
        binary_str = format(shifted_val, '08b')   # Step 3: Convert to 8-bit binary string
        final_bits = binary_str[:7]               # Step 4: Take the first 7 bits only
        encrypted_list.append(final_bits)

    return ' '.join(encrypted_list)


# Main program
if __name__ == "__main__":
    user_input = input("Enter a message: ")
    print(encrypt_message(user_input))

