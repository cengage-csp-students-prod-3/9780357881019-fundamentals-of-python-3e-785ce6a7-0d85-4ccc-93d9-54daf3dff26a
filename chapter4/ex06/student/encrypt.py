# encrypt.py

def char_to_encrypted_bits(char):
    # Step 1: ASCII value + 1
    ascii_plus_one = ord(char) + 1

    # Step 2: Shift left by 1
    shifted = ascii_plus_one << 1

    # Step 3: Convert to binary string, remove "0b"
    return bin(shifted)[2:]

def main():
    message = input("Enter a message: ")
    encrypted_bits = [char_to_encrypted_bits(c) for c in message]
    print(' '.join(encrypted_bits))

if __name__ == "__main__":
    main()



