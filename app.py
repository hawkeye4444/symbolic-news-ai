# symbolic_news_ai/app.py

"""
AI-Powered Symbolic Pattern Recognition System for News and Media Analysis
Free to deploy using Streamlit, Python, and public APIs
"""

import streamlit as st
import feedparser
from datetime import datetime
from modules.gematria import calculate_all_ciphers
from modules.numerology import analyze_date, compare_intervals
from modules.astro import get_astrological_data
from modules.nlp import extract_entities_and_keywords
from modules.patterns import recognize_patterns
from modules.interpretation import generate_symbolic_narrative

# --- UI Layout ---
st.set_page_config(page_title="Symbolic Event Scanner", layout="wide")
st.title("🧠 Symbolic Pattern Recognition for News & Media")

st.sidebar.header("News Input")
source = st.sidebar.text_input("RSS Feed URL", "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
sort_by_score = st.sidebar.checkbox("Sort by Ritual Score", value=True)

results = []

if st.sidebar.button("Ingest & Analyze"):
    feed = feedparser.parse(source)

    for entry in feed.entries[:5]:
        full_text = entry.title + " " + entry.summary
        entities, keywords = extract_entities_and_keywords(full_text)
        gematria_results = calculate_all_ciphers(entities + keywords)
        try:
            date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
        except:
            date = datetime.now()
        numerology_result = analyze_date(date)
        astro_data = get_astrological_data(date)
        patterns = recognize_patterns(entities, keywords, gematria_results)

        # --- Relevance Filter ---
        is_relevant = bool(keywords or patterns or numerology_result['reduced'] in [33, 88, 203, 322, 105])
        if not is_relevant:
            continue

        # --- Ritual Scoring ---
        ritual_score = 0
        ritual_score += len(patterns) * 5
        ritual_score += len(keywords) * 2
        if numerology_result['reduced'] in [33, 88, 203, 322, 105]:
            ritual_score += 3
        if astro_data['moon_phase'] in ["Full Moon", "New Moon"]:
            ritual_score += 2

        results.append({
            "title": entry.title,
            "published": entry.published,
            "entities": entities,
            "keywords": keywords,
            "gematria": gematria_results,
            "numerology": numerology_result,
            "astro": astro_data,
            "patterns": patterns,
            "ritual_score": ritual_score
        })

    if sort_by_score:
        results = sorted(results, key=lambda x: x['ritual_score'], reverse=True)

    for item in results:
        st.markdown("---")
        st.subheader(item['title'])
        st.caption(item['published'])
        st.write("**Ritual Score**:", f"{item['ritual_score']} / 15")
        st.write("**Entities**:", item['entities'])
        st.write("**Keywords**:", item['keywords'])
        st.json(item['gematria'])
        st.write("**Date Numerology**:", item['numerology'])
        st.write("**Celestial Snapshot**:", item['astro'])
        st.write("**Pattern Matches**:", item['patterns'])

        narrative = generate_symbolic_narrative(
            item['title'],
            item['entities'],
            datetime.now(),
            item['gematria'],
            item['numerology'],
            item['keywords'],
            item['astro'],
            item['patterns']
        )
        st.success(narrative)

st.sidebar.markdown("""
This system:
- Extracts entities and symbolic words
- Calculates gematria
- Decodes numerology and astrology
- Recognizes ritualistic structures
- Filters for symbolically relevant news
- Scores and sorts news by ritual intensity
- Outputs interpretations and predictive syncs
""")