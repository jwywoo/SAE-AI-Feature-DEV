import re


def text_cleaning(text):
    if isinstance(text, str):
        # lower case
        text = text.lower()
        # empty space removal
        text = text.strip()
        # multiple empty space removal
        text = re.sub(r'\s+', ' ', text)
        # special character removal
        text = re.sub(r'[^\w\s.,!?$%&@-]', '', text)
    return text
