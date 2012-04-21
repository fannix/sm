""" project text to libsvm vector space
"""

from gensim import corpora, models, similarities
import sys
import os.path

def load_document():
    text_li = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        text_li.append(line)

    document_li = [text.split() for text in text_li]

    return document_li

def main():
    usage = "Usage: %prog outfile vocabfile < infile"
    if len(sys.argv) != 3:
        print usage
        sys.exit(-1)
    outfile = sys.argv[1]
    vocabfile = sys.argv[2]

    document_li = load_document()

    vocab_bin = vocabfile + '.bin'
    if os.path.exists(vocab_bin):
        vocab = corpora.Dictionary.load(vocab_bin)

    else:
        vocab = corpora.Dictionary(document_li)
        vocab.filter_extremes(no_below=3, no_above=0.4)
        vocab.save(vocab_bin)
        vocab.save_as_text(vocabfile+'.txt')

    corpus = [vocab.doc2bow(doc) for doc in document_li]

    corpora.SvmLightCorpus.serialize(outfile, corpus)

if __name__ == "__main__":
    main()
