# Word categories
articles = {"A", "THE"}
nouns = {"BOY", "GIRL", "BALL", "BAT"}
verbs = {"HIT", "SAW", "LIKED"}
prepositions = {"WITH", "BY"}
adjectives = {"RED", "BIG", "SMALL"}  # New: adjectives
conjunctions = {"AND", "BUT", "OR"}   # New: conjunctions


def isSentence(words):
    """Checks if a sentence is grammatically correct."""
    # Try parsing the first clause
    remaining = parseClause(words)
    if remaining is None:
        return False

    # If there's no conjunction, the sentence is valid
    if not remaining:
        return True

    # If next word is a conjunction, parse the second clause
    if remaining[0] in conjunctions:
        remaining = parseClause(remaining[1:])
        return remaining == []

    # If leftover words without a conjunction: invalid
    return False


def parseClause(words):
    """Parses a clause consisting of a noun phrase and a verb phrase."""
    remaining = parseNounPhrase(words)
    if remaining is None:
        return None
    remaining = parseVerbPhrase(remaining)
    return remaining


def parseNounPhrase(words):
    """Parses a noun phrase: ARTICLE [ADJECTIVE] NOUN"""
    if len(words) < 2 or words[0] not in articles:
        return None

    if words[1] in adjectives:
        # ARTICLE + ADJECTIVE + NOUN
        if len(words) < 3 or words[2] not in nouns:
            return None
        return words[3:]
    elif words[1] in nouns:
        # ARTICLE + NOUN
        return words[2:]
    else:
        return None


def parseVerbPhrase(words):
    """Parses a verb phrase: VERB + NOUN_PHRASE [+ PREPOSITIONAL_PHRASE (optional)]"""
    if len(words) < 2 or words[0] not in verbs:
        return None

    remaining = parseNounPhrase(words[1:])
    if remaining is None:
        return None

    # Optionally parse prepositional phrase
    if remaining and remaining[0] in prepositions:
        remaining = parsePrepositionalPhrase(remaining)
    return remaining


def parsePrepositionalPhrase(words):
    """Parses a prepositional phrase: PREPOSITION + NOUN_PHRASE"""
    if len(words) < 2 or words[0] not in prepositions:
        return None
    return parseNounPhrase(words[1:])


def main():
    while True:
        sentence = input("Enter a sentence or press return to quit: ")
        if sentence == "":
            break
        words = sentence.upper().split()
        if isSentence(words):
            print("Ok, grammatically correct")
        else:
            print("Not grammatically correct")


if __name__ == "__main__":
    main()
