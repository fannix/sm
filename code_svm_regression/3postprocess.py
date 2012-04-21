#encoding: utf-8
"""
Postprocess text

Possible operations include:
    filter stopwords
    filter punctuations
    filter infrequent words
    combine words into phrases
    introduce sentiment dictionary
"""
import sys


def read_dict(filename):
    """Read dictionary file
    """
    dictionary = set()
    with open(filename) as f:
        for line in f:
            line = line.decode("utf-8")
            word = line.strip()
            dictionary.add(word)

    return dictionary


def add_sentiment_feature(line, pos_lexicon, neg_lexicon):
    word_li = line.strip().split()
    word_set = set(word_li)

    pos_count = len(word_set.intersection(pos_lexicon))
    neg_count = len(word_set.intersection(neg_lexicon))
    if pos_count > neg_count and pos_count > 0:
        word_li.append("POS_WORD")
    elif neg_count >= pos_count and neg_count > 0:
        word_li.append("NEG_WORD")

    return " ".join(word_li)


def main():
    pos_lexicon = read_dict("code_svm_regression/positive_submit.txt")
    neg_lexicon = read_dict("code_svm_regression/negative_submit.txt")
    #print >> sys.stderr, len(pos_lexicon)

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        line = line.decode("gb18030")
        new_line = add_sentiment_feature(line, pos_lexicon, neg_lexicon)
        print new_line.encode("utf-8")

if __name__ == "__main__":
    main()
