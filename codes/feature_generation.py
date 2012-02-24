"""
Generate a feature file for a text file with labels

Each line in a text file is a document and its label. 
Generate a SVMLight style file.
"""

import sys


def generate_feature(docs):
    """
    Generate features from documents

    docs: list of doc, which is a text string and a label separated by \t
    """
    vocabulary = {}
    for a_doc in docs:
        text, label = a_doc.split('\t')
        words = text.split()
        feature_set = set()
        for a_word in words:
            if a_word not in vocabulary:
                vocabulary[a_word] = len(vocabulary) + 1
            word_idx = vocabulary[a_word]
            feature_set.add(word_idx)
        feature_li = []
        for e in feature_set:
            feature_li.append("%d:1" % e)
        print label+'\t' + " ".join(feature_li)
    
    vocab_li = [(idx, word) for (word, idx) in vocabulary.items()]
    vocab_li.sort()
    with open("vocab", 'w') as f:
        for (idx, word) in vocab_li:
            f.write("%d\t%s\n" % (idx, word))

if __name__ == "__main__":
    docs = []
    for line in sys.stdin:
        docs.append(line.strip())
    generate_feature(docs)
