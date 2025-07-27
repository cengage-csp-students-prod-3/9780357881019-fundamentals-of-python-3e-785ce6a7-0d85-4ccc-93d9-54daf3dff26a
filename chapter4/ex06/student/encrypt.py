# encrypt.py

def char_to_encrypted_bits(char):
    # Step 1: Get ASCII + 1
    ascii_plus_one = ord(char) + 1

    # Step 2: Convert to binary (remove '0b')
    binary = bin(ascii_plus_one)[2:]

    # Step 3: Shift bits left by 1 (string shift)
    shifted = binary[1:] + '0'

    return shifted

def main():
    message = input("Enter a message: ")
    encrypted = [char_to_encrypted_bits(c) for c in message]
    print(' '.join(encrypted))

if __name__ == "__main__":
    main()




