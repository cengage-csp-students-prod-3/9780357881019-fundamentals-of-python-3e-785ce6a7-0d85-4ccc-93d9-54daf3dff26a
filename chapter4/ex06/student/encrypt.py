# encrypt.py

def encrypt_message(message):
    encrypted_list = []

    for char in message:
        ascii_val = ord(char) + 1  # Step 1: Add 1 to ASCII
        shifted_val = (ascii_val << 1) & 0b1111111  # Step 2–4: Shift left, keep 7 bits
        binary_str = format(shifted_val, '07b')     # Step 5: Convert to 7-bit binary string
        encrypted_list.append(binary_str)

    return ' '.join(encrypted_list)


# Main program
if __name__ == "__main__":
    user_input = input("Enter a message: ")
    print(encrypt_message(user_input))






