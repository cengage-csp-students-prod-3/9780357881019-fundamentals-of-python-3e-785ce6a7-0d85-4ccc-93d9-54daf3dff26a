# generator.py

import random

def getWords(filename):
    """Reads words from a file, strips whitespace, uppercases them, and returns a tuple."""
    with open(filename, 'r') as file:
        return tuple(line.strip().upper() for line in file if line.strip())

def generate_sentence():
    """Generates a sentence following the structure:
    article + noun + verb + article + noun + preposition + article + noun
    """
    return (
        random.choice(articles) + ' ' +
        random.choice(nouns) + ' ' +
        random.choice(verbs) + ' ' +
        random.choice(articles) + ' ' +
        random.choice(nouns) + ' ' +
        random.choice(prepositions) + ' ' +
        random.choice(articles) + ' ' +
        random.choice(nouns)
    )

# Load vocabulary from files
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

# Main program
def main():
    try:
        count = int(input("Enter the number of sentences: "))
        print()
        for _ in range(count):
            print(generate_sentence())
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
