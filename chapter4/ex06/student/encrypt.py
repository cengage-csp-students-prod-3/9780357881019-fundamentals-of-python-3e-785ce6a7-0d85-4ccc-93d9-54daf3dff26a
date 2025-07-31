# Decrypt Caesar cipher for printable ASCII characters (32–126)

coded_text = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))

decrypted = ""

for ch in coded_text:
    ascii_val = ord(ch)
    if 32 <= ascii_val <= 126:
        shifted = (ascii_val - 32 - distance) % 95 + 32
        decrypted += chr(shifted)
    else:
        decrypted += ch  # leave non-printable characters as-is

print(decrypted)




