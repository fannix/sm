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

    new_text = text
    new_text = re.sub(url_pattern, " URL_RE ", new_text)
    new_text = re.sub(at_pattern, " AT_RE ", new_text)
    if re.search(emoticon_pattern, new_text):
        new_text = new_text + " EMOTICON_RE"
    if re.search(hashtag_pattern, new_text):
        new_text = new_text + " HASHTAG_RE"

    return new_text

def test_normalize_text():
    """
    unit test of normalize_text()
    """
    assert normalize_text("ab http://www.google.com") == "ab  URL_RE "
    assert normalize_text("ab @abd") == "ab  AT_RE "
    assert normalize_text("ab [abd]") == "ab [abd] EMOTICON_RE"
    assert normalize_text("ab #abd#") == "ab #abd# HASHTAG_RE"

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        new_line = normalize_text(line)
        print new_line
