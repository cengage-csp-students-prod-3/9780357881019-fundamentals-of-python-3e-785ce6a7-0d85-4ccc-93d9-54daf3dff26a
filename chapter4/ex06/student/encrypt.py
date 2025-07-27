# encrypt.py

def char_to_encrypted_bits(char):
    # Step 1: Get ASCII value and add 1
    value = ord(char) + 1

    # Step 2: Bitwise shift left by 1
    shifted_value = value << 1

    # Step 3: Convert to binary (no '0b' prefix)
    return bin(shifted_value)[2:]

def main():
    message = input("Enter a message: ")
    encrypted = [char_to_encrypted_bits(c) for c in message]
    print(' '.join(encrypted))

if __name__ == "__main__":
    main()



