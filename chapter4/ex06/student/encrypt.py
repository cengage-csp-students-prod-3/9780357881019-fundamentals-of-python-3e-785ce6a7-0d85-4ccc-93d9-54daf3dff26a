# encrypt.py

def encrypt_message(message):
    encrypted_list = []

    for char in message:
        ascii_val = ord(char) + 1               # Step 1: Add 1 to ASCII value
        binary_str = format(ascii_val, '08b')   # Step 2: Convert to 8-bit binary string
        shifted_str = binary_str[1:] + '0'      # Step 3: Shift bits left by 1 (drop first, add '0')
        encrypted_list.append(shifted_str)      # Step 4: Add to list

    return ' '.join(encrypted_list)             # Step 5: Join with single space


# Main program
if __name__ == "__main__":
    user_input = input("Enter a message: ")
    encrypted_output = encrypt_message(user_input)
    print(encrypted_output)

