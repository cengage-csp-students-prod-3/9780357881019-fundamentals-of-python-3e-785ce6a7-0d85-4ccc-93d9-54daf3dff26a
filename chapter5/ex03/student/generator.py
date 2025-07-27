def getWords(filename):
    """
    Reads a file containing one word per line and returns a tuple of words in uppercase.
    :param filename: The name of the text file to read.
    :return: A tuple containing all words from the file.
    """
    words = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().upper()
            if word:
                words.append(word)
    return tuple(words)
