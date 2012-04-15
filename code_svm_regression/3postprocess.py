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

def filter_nothing(line):
    return line

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        new_line = filter_nothing(line)
        print new_line

if __name__ == "__main__":
    main()
