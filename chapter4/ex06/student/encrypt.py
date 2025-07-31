# encrypt.py

import sys

# Use sys.stdin.read() to support non-interactive test environments
message = sys.stdin.read().strip()

# Convert to binary (example: 7-bit ASCII format)
binary_values = [format(ord(char), '07b') for char in message]

# Format output as a list containing a space-separated string
output = [" ".join(binary_values)]

print(output)






