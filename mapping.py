import json
from difflib import SequenceMatcher

with open("phrases.json", "r", encoding="utf-8") as f:
    phrases = json.load(f)

def best_match(text):
    text = text.lower().strip()
    best_phrase= None
    highest_ratio = 0.0
    for phrase in phrases.keys():
        ratio = SequenceMatcher(None, text.lower(), phrase.lower()).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_phrase = phrase
    if highest_ratio > 0.7:
        return phrases[best_phrase]
    else:
        print("⚠️ No close match found.")
        return None
