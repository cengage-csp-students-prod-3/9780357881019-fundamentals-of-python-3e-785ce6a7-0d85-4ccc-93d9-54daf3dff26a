# encrypt.py

def encrypt_message(message):
    encrypted_list = []

    for char in message:
        # Step 1: Get ASCII value and add 1
        ascii_val = ord(char) + 1

        # Step 2: Convert to binary string
        binary_str = ''
        number = ascii_val
        while number > 0:
            binary_str = str(number % 2) + binary_str
            number = number // 2

        # Step 3: Bit shift left by 1 (drop first bit, add '0' at the end)
        shifted_str = binary_str[1:] + '0' if len(binary_str) > 1 else '0'

        # Step 4: Append to result list
        encrypted_list.append(shifted_str)

    # Step 5: Join with single space and return
    return ' '.join(encrypted_list)


# Main program
if __name__ == "__main__":
    user_input = input("Enter a message: ")
    encrypted_output = encrypt_message(user_input)
    print(encrypted_output)





