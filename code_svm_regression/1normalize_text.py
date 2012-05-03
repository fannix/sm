"""
Normalization text

Sustitute the HTTP pattern, emoticon pattern and  AT pattern
"""

import sys
import re

def normalize_text(text):
    """
    normalize text

    text: a string of text
    return: normalized text
    """
    url_pattern = r"(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?"
    at_pattern = r"@[^@ ]+"
    emoticon_pattern = r"\[[^\[\]]+\]"
    hashtag_pattern = r"#[^# ]+#"
    phone_pattern = r"\d{11}"
    number_pattern = "\d+(\.\d+)?"

    new_text = text
    new_text = re.sub(url_pattern, " URLRE ", new_text)
    new_text = re.sub(at_pattern, " ATRE ", new_text)
    new_text = re.sub(phone_pattern, " PHONERE ", new_text)
    new_text = re.sub(number_pattern, " NUMBERRE ", new_text)

    found = re.findall(emoticon_pattern, new_text)
    for e in set(found):
        new_text = new_text.replace(e, e + " EMOTICONRE ")
    found = re.findall(hashtag_pattern, new_text)
    for e in set(found):
        new_text = new_text.replace(e, e + " HASHTAGRE ")

    return new_text

def test_normalize_text():
    """
    unit test of normalize_text()
    """
    assert normalize_text("ab http://www.google.com") == "ab  URLRE "
    assert normalize_text("ab @abd") == "ab  ATRE "
    assert normalize_text("ab [abd]") == "ab [abd] EMOTICONRE "
    assert normalize_text("ab [abd] [bcd]") == "ab [abd] EMOTICONRE  [bcd] EMOTICONRE "
    assert normalize_text("ab #abd#") == "ab #abd# HASHTAGRE "
    assert normalize_text("15901256081") == " PHONERE "
    assert normalize_text("159.0") == " NUMBERRE "
    assert normalize_text("159") == " NUMBERRE "


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            line = "AnEmptyTag"

        new_line = normalize_text(line)
        print new_line
