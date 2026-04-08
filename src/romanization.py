"""
Romanization Pipeline for Indic Languages
==========================================
Converts Indic language text (native script) to romanized form.
Uses the Indic NLP Library for transliteration.

Supported languages: Gujarati, Hindi, Malayalam, Marathi, Tamil

Author: G L John Salvin, IIT Palakkad (2026)
"""

# NOTE: Requires indic-nlp-library to be installed
# pip install indic-nlp-library

LANGUAGE_CODES = {
    "Gujarati": "gu",
    "Hindi": "hi",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Tamil": "ta",
}


def romanize_text(text, lang_code):
    """
    Romanize a single text string from a given Indic language.

    Args:
        text (str): Input text in native script.
        lang_code (str): ISO 639-1 language code (e.g., 'ta' for Tamil).

    Returns:
        str: Romanized text.
    """
    try:
        from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
        romanized = UnicodeIndicTransliterator.transliterate(text, lang_code, "en")
        return romanized
    except ImportError:
        raise ImportError(
            "indic-nlp-library is required. Install with: pip install indic-nlp-library"
        )


def romanize_dataset(texts, language):
    """
    Romanize a list of texts for a given language.

    Args:
        texts (list[str]): List of texts in native script.
        language (str): Language name (e.g., 'Tamil').

    Returns:
        list[str]: Romanized texts.
    """
    lang_code = LANGUAGE_CODES.get(language)
    if lang_code is None:
        raise ValueError(f"Unsupported language: {language}. Choose from {list(LANGUAGE_CODES.keys())}")

    return [romanize_text(t, lang_code) for t in texts]


if __name__ == "__main__":
    sample_texts = {
        "Tamil": "நான் வீட்டிற்கு செல்கிறேன்",
        "Hindi": "मैं घर जा रहा हूँ",
        "Malayalam": "ഞാൻ വീട്ടിലേക്ക് പോകുന്നു",
    }
    for lang, text in sample_texts.items():
        try:
            roman = romanize_text(text, LANGUAGE_CODES[lang])
            print(f"{lang}: {text} → {roman}")
        except ImportError as e:
            print(f"[{lang}] {e}")
