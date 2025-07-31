# generator.py

import random

def getWords(filename):
    """Reads words from the given file, returns them as a tuple in uppercase."""
    word_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                if word:
                    word_list.append(word.upper())  # Ensures output is in uppercase
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()
    return tuple(word_list)

def generate_sentence():
    """Generates a random sentence using the defined grammar."""
    return (random.choice(articles) + ' ' +
            random.choice(nouns) + ' ' +
            random.choice(verbs) + ' ' +
            random.choice(articles) + ' ' +
            random.choice(nouns) + ' ' +
            random.choice(prepositions) + ' ' +
            random.choice(articles) + ' ' +
            random.choice(nouns))

# Load vocabulary from files
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
articles = getWords("articles.txt")
prepositions = getWords("prepositions.txt")

# Main program
def main():
    try:
        num_sentences = int(input("Enter the number of sentences: "))
        for _ in range(num_sentences):
            print(generate_sentence())
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
