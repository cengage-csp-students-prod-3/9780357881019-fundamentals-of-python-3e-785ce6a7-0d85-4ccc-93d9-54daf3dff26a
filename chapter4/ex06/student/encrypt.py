# encrypt.py

def char_to_encrypted_bits(char):
    # Step 1: Get ASCII value and add 1
    ascii_value = ord(char) + 1

    # Step 2: Convert to 8-bit binary string
    binary_string = format(ascii_value, '08b')

    # Step 3: Bit shift left by 1 (circular)
    shifted_binary = binary_string[1:] + '0'

    return shifted_binary

# Main program
def main():
    message = input("Enter a message: ")
    encrypted_bits = [char_to_encrypted_bits(char) for char in message]
    encrypted_message = ' '.join(encrypted_bits)
    print(encrypted_message)

if __name__ == "__main__":
    main()

