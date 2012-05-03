"""
Split original tweet and retweet
"""

def split_tweet(line):
    if not line:
        return ("AnEmptyTag", "AnEmptyTag")
    index = line.find("//")
    if index != -1:
        li =  [line[:index], line[index+2:]]

    else:
        li = [line, "AnEmptyTag"]

    if not li[0].strip():
        li[0] = "AnEmptyTag"
    return li

def test_split_tweet():
    test_str = "ab//cd//ef"
    li = split_tweet(test_str)
    print li
    assert li[0] == "ab"
    assert li[1] == "cd//ef"

    test_blank = "ab"
    li = split_tweet(test_blank)
    assert li[0] == "ab"
    assert li[1] == "AnEmptyTag"

    test_total_blank = " "
    li = split_tweet(test_total_blank)
    assert li[0] == "AnEmptyTag"
    assert li[1] == "AnEmptyTag"

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        original, retweet = split_tweet(line.strip())
        print original + "\t" + retweet
