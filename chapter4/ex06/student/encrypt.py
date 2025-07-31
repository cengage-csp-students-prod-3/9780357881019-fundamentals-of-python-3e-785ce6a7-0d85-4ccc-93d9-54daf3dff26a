# encrypt.py

def encrypt_message(message):
    encrypted_list = []

    for char in message:
        ascii_val = ord(char) + 1                 # Step 1
        shifted_val = (ascii_val << 1) & 0xFF     # Step 2 & 3 (keep 8 bits only)
        binary_str = format(shifted_val, '08b')   # Step 4: 8-bit string
        final_bits = binary_str[:7]               # Step 5: take first 7 bits only
        encrypted_list.append(final_bits)

    return ' '.join(encrypted_list)


# Main program
if __name__ == "__main__":
    user_input = input("Enter a message: ")
    print(encrypt_message(user_input))
