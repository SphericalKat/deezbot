import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Define a function to check if a noun immediately follows a verb
def is_noun_follows_verb(text: str) -> bool:
    doc = nlp(text)
    for i in range(len(doc) - 1):
        print(doc[i].pos_, doc[i].text, doc[i + 1].pos_, doc[i + 1].text)
        # Check if the current token is a verb and the next token is a noun
        if doc[i].pos_ == "VERB" and doc[i + 1].pos_ in ["NOUN", "PROPN", "PRON"]:
            return True, doc[i].lemma_

    return False, None


def find_exploitable_phrases(sentence):
    # Parse the sentence using spaCy
    doc = nlp(sentence)
    exploitable_phrases = []

    for token in doc:
        if token.pos_ == "VERB":
            # Collect the verb and its relevant preceding words
            phrase = [token.lemma_]
            preceding_tokens = []

            # Collect adverbs and prepositions that are syntactically dependent on the verb
            # eg: I am testing for bugs. -> "for" is dependent on "testing"
            for child in token.children:
                if child.dep_ in {"advmod", "neg", "prep"}:
                    preceding_tokens.append(child)

            # Sort the preceding tokens by their position in the sentence
            # this makes it sound natural
            preceding_tokens = sorted(preceding_tokens, key=lambda x: x.i)

            # Add the sorted preceding tokens to the phrase
            # depending on certain conditions
            for t in preceding_tokens:
                # if the token is a preposition, add the preposition and its dependent to the phrase
                if t.dep_ == "prep":
                    phrase.append(t.text)

                    # if the preposition has a dependent which is a 
                    # prepositional complement, add the dependent to the phrase
                    for subchild in t.children:
                        if subchild.dep_ in {"pcomp"}:
                            phrase.append(subchild.text)
                # otherwise, add the token to the beginning of the phrase
                else:
                    phrase.insert(0, t.text)

            phrase_text = " ".join(phrase)
            exploitable_phrases.append(phrase_text)

    return exploitable_phrases


if __name__ == "__main__":
    # Test the function
    sentences = [
        "I am testing for bugs.",
        "She was speaking at a conference.",
        "He is looking into the issue.",
        "They are working on the project.",
        "Apple is looking at buying U.K. startup for $1 billion",
    ]

    for sentence in sentences:
        phrases = find_exploitable_phrases(sentence)
        for phrase in phrases:
            print(f"Original phrase: {sentence}")
            print(f"Exploitable phrase: {phrase} deez")
            print()
