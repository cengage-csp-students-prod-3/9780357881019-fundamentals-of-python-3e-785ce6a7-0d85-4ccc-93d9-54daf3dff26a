# encrypt.py

def char_to_encrypted_bits(char):
    # Step 1: ASCII + 1
    ascii_plus_one = ord(char) + 1  # 👈 THIS WAS MISSING EARLIER

    # Step 2: Convert to 8-bit binary
    binary_str = format(ascii_plus_one, '08b')

    # Step 3: Shift left by one bit (as string)
    shifted = binary_str[1:] + '0'

    return shifted

def main():
    message = input("Enter a message: ")
    encrypted = [char_to_encrypted_bits(c) for c in message]
    print(' '.join(encrypted))

if __name__ == "__main__":
    main()



