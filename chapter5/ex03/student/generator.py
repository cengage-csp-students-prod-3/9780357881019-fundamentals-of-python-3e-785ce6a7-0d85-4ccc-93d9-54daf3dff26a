# generator.py

import random

def getWords(filename):
    """Reads words from a given file and returns them as an uppercase tuple in file order."""
    with open(filename, 'r') as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return tuple(words)

def sentence():
    """Generates a sentence using the grammar structure."""
    return f"{random.choice(articles)} {random.choice(nouns)} " \
           f"{random.choice(verbs)} {random.choice(articles)} " \
           f"{random.choice(nouns)} {random.choice(prepositions)} " \
           f"{random.choice(articles)} {random.choice(nouns)}"

# Load words from files
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
articles = getWords("articles.txt")
prepositions = getWords("prepositions.txt")

# Main program
def main():
    try:
        count = int(input("Enter the number of sentences: "))
        print()
        for _ in range(count):
            print(sentence())
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
