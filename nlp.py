import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Define a function to check if a noun immediately follows a verb
def is_noun_follows_verb(text: str) -> bool:
    doc = nlp(text)
    for i in range(len(doc) - 1):
        # Check if the current token is a verb and the next token is a noun
        if doc[i].pos_ == "VERB" and doc[i + 1].pos_ in ["NOUN", "PROPN", "PRON"]:
            return True, doc[i].lemma_
    
    return False, None


if __name__ == "__main__":
    text = "I was eating pizza"
    is_follows_verb, verb = is_noun_follows_verb(text)
    if is_follows_verb:
        print(f"{verb} deez")
    else:
        print("No noun follows a verb in the text")