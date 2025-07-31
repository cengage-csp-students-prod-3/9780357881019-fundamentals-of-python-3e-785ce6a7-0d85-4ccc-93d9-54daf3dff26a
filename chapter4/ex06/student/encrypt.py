# encrypt.py

def encrypt_message(message):
    encrypted_bits = []

    for char in message:
        # Step 1: Get ASCII value and add 1
        ascii_val = ord(char) + 1

        # Step 2: Convert to 8-bit binary string
        binary_str = format(ascii_val, '08b')

        # Step 3: Left shift the bit string by 1
        # Drop the first bit and add a '0' at the end
        shifted = binary_str[1:] + '0'

        # Step 4: Add to the encrypted list
        encrypted_bits.append(shifted)

    # Step 5: Join all with spaces
    return ' '.join(encrypted_bits)

# Main program
if __name__ == "__main__":
    message = input("Enter a message: ")
    encrypted = encrypt_message(message)
    print(encrypted)



