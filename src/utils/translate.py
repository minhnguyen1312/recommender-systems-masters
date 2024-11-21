from deep_translator import GoogleTranslator

def translate_text_german_english(text, source_lang="german", target_lang="english"):
    """
        This utility func is used to translate german to english
    """
    translator = GoogleTranslator(from_lang=source_lang, to_lang=target_lang)
    translation = translator.translate(text)
    return translation