"""
Normalize the text file

Normalize the label to 1/0/-1
Substitute the number and URLs
"""

import sys
import re

def test_normalize_text():
    """
    unit test of normalize_text()
    """
    assert normalize_text("ab http://www.google.com") == "ab  URL_RE "
    assert normalize_text("ab @abd") == "ab  AT_RE "
    assert normalize_text("ab [abd]") == "ab [abd] EMOTICON_RE"

def normalize_text(text):
    """
    normalize text

    text: a string of text
    return: normalized text
    """

    url_pattern = r"(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?"
    at_pattern = r"@[^@ ]+"
    emoticon_pattern = r"\[[^\[\]]+\]"

    new_text = text
    new_text = re.sub(url_pattern, " URL_RE ", new_text)
    new_text = re.sub(at_pattern, " AT_RE ", new_text)
    if re.search(emoticon_pattern, new_text):
        new_text = new_text + " EMOTICON_RE"

    return new_text

def normalize(sample):
    """
    Normalize a sample

    sample: text + "\t" + label
    """
    text, label = sample.split('\t')
    new_text = normalize_text(text)
    label_int = int(label)
    if label_int < 0:
        new_label = -1
    elif label_int > 0:
        new_label = 1
    else:
        new_label = 0

    print "%s\t%d" % (new_text, new_label)


if __name__ == "__main__":
    for line in sys.stdin:
        normalize(line.strip())
