# Grammar categories
articles = {"A", "THE"}
nouns = {"BOY", "GIRL", "BALL", "BAT"}
verbs = {"HIT", "SAW", "LIKED"}
prepositions = {"WITH", "BY"}
adjectives = {"RED", "BIG", "SMALL"}  # New support
conjunctions = {"AND", "BUT", "OR"}   # New support

def parseNounPhrase(words):
    """Parses a noun phrase: ARTICLE [ADJECTIVE] NOUN"""
    if len(words) < 2 or words[0] not in articles:
        return None

    if words[1] in adjectives:
        if len(words) < 3 or words[2] not in nouns:
            return None
        return words[3:]
    elif words[1] in nouns:
        return words[2:]
    else:
        return None

def parseVerbPhrase(words):
    """Parses a verb phrase: VERB + NOUN_PHRASE [+ PREPOSITIONAL_PHRASE (optional)]"""
    if not words or words[0] not in verbs:
        return None

    remaining = parseNounPhrase(words[1:])
    if remaining is None:
        return None

    if remaining and remaining[0] in prepositions:
        remaining = parsePrepositionalPhrase(remaining)
        if remaining is None:
            return None

    return remaining

def parsePrepositionalPhrase(words):
    """Parses a prepositional phrase: PREPOSITION + NOUN_PHRASE"""
    if len(words) < 2 or words[0] not in prepositions:
        return None

    return parseNounPhrase(words[1:])

def parseClause(words):
    """Parses a clause consisting of a noun phrase and a verb phrase."""
    remaining = parseNounPhrase(words)
    if remaining is None:
        return None

    remaining = parseVerbPhrase(remaining)
    if remaining is None:
        return None

    return remaining

def isSentence(words):
    """Determines if the sentence is grammatically correct."""
    remaining = parseClause(words)
    if remaining is None:
        return False

    if not remaining:
        return True

    if remaining[0] in conjunctions:
        remaining = parseClause(remaining[1:])
        return remaining == []

    return False

def main():
    while True:
        sentence = input("Enter a sentence or press return to quit: ")
        if sentence == "":
            break
        words = sentence.upper().split()
        if isSentence(words):
            print("[correct]")
        else:
            print("[incorrect]")

