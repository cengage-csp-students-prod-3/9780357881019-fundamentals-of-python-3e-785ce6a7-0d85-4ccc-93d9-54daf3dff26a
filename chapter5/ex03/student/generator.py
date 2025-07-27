def getWords(filename):
    """
    Reads a file containing one word per line and returns a tuple of uppercase words.
    """
    with open(filename, 'r') as file:
        # Read all lines, strip whitespace, convert to uppercase, and ignore empty lines
        words = [line.strip().upper() for line in file if line.strip()]
    return tuple(words)
