# Grammar categories
articles = {"A", "THE"}
nouns = {"BOY", "GIRL", "BALL", "BAT"}
verbs = {"HIT", "SAW", "LIKED"}
prepositions = {"WITH", "BY"}
adjectives = {"RED", "BIG", "SMALL"}  # Adjectives supported
conjunctions = {"AND", "BUT", "OR"}   # Conjunctions supported


# --- Grammar Parsing Functions (Core Logic) ---

def parseNounPhrase(words):
    if len(words) < 2 or words[0] not in articles:
        return None
    if words[1] in adjectives:
        if len(words) < 3 or words[2] not in nouns:
            return None
        return words[3:]
    elif words[1] in nouns:
        return words[2:]
    return None


def parseVerbPhrase(words):
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
    if len(words) < 2 or words[0] not in prepositions:
        return None
    return parseNounPhrase(words[1:])


def parseClause(words):
    remaining = parseNounPhrase(words)
    if remaining is None:
        return None
    remaining = parseVerbPhrase(remaining)
    if remaining is None:
        return None
    return remaining


def isSentence(words):
    remaining = parseClause(words)
    if remaining is None:
        return False
    if not remaining:
        return True
    if remaining[0] in conjunctions:
        remaining = parseClause(remaining[1:])
        return remaining == []
    return False


# --- Functions Required by Test System ---

def nounPhrase(words):
    result = parseNounPhrase(words)
    if result is not None:
        print("[correct]")
    else:
        print("[incorrect]")


def verbPhrase(words):
    result = parseVerbPhrase(words)
    if result is not None:
        print("[correct]")
    else:
        print("[incorrect]")


def sentence(words):
    if isSentence(words):
        print("[correct]")
    else:
        print("[incorrect]")


# --- Optional CLI Entry Point ---

def main():
    while True:
        sentence_input = input("Enter a sentence or press return to quit: ")
        if sentence_input == "":
            break
        words = sentence_input.upper().split()
        sentence(words)  # Uses wrapper that prints [correct]/[incorrect]


if __name__ == "__main__":
    main()

