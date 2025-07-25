def generate_symbolic_narrative(title, entities, date, gematria, numerology, keywords, astrology, patterns):
    symbols = ", ".join(set(k["meaning"] for k in patterns))
    summary = f"Event '{title}' shows symbolic resonance with {symbols}. "
    summary += f"Astrological influence from Saturn at {astrology['saturn_position']} degrees. "
    summary += f"Date numerology reduces to {numerology['reduced']}."
    return summary