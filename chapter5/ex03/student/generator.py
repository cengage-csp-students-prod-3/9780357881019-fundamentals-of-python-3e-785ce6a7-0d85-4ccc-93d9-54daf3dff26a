# generator.py

import random

def getWords(filename):
    """Reads words from a given file and returns them as a tuple."""
    words = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip().upper()  # Optional: convert to uppercase
                if word:
                    words.append(word)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit()
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
