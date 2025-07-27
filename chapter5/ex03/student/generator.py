def getWords(filename):
    with open(filename, 'r') as file:
        return tuple(line.strip().upper() for line in file if line.strip())
