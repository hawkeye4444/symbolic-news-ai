KNOWN_VALUES = {
    33: "Freemasonry",
    203: "Ritual",
    105: "Masonry",
    81: "Blood Ritual"
}

def recognize_patterns(entities, keywords, gematria_results):
    matches = []
    for term, values in gematria_results.items():
        for cipher, val in values.items():
            if val in KNOWN_VALUES:
                matches.append({"term": term, "cipher": cipher, "value": val, "meaning": KNOWN_VALUES[val]})
    return matches