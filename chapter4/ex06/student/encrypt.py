# encrypt.py

def char_to_encrypted_bits(char):
    # Step 1: Get ASCII value and add 1
    ascii_plus_one = ord(char) + 1

    # Step 2: Convert to binary string (no padding)
    binary_string = bin(ascii_plus_one)[2:]

    # Step 3: Shift bits left by 1 (drop MSB, add '0' at the end)
    shifted_binary = binary_string[1:] + '0' if len(binary_string) > 1 else '0'

    return shifted_binary

def main():
    message = input("Enter a message: ")
    encrypted = [char_to_encrypted_bits(c) for c in message]
    print(' '.join(encrypted))

if __name__ == "__main__":
    main()


