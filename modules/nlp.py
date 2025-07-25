import spacy

try:
    import en_core_web_sm
    nlp = en_core_web_sm.load()
except ImportError:
    from spacy.cli import download
    download("en_core_web_sm")
    import en_core_web_sm
    nlp = en_core_web_sm.load()

SYMBOLIC_KEYWORDS = ["ritual", "sacrifice", "phoenix", "saturn", "rebirth"]

def extract_entities_and_keywords(text):
    doc = nlp(text)
    entities = list(set([ent.text for ent in doc.ents]))
    keywords = [kw for kw in SYMBOLIC_KEYWORDS if kw in text.lower()]
    return entities, keywords
