
import re

CIPHERS = {
    "English Ordinal": lambda c: ord(c) - 64,
    "Reverse Ordinal": lambda c: 27 - (ord(c) - 64),
    "Full Reduction": lambda c: (ord(c) - 64 - 1) % 9 + 1,
}

def clean_text(text):
    return re.sub(r"[^A-Z]", "", text.upper())

def calculate_all_ciphers(terms):
    results = {}
    for term in terms:
        clean = clean_text(term)
        results[term] = {
            cipher: sum(fn(c) for c in clean)
            for cipher, fn in CIPHERS.items()
        }
    return results
