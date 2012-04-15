"""
Label an instance by aggregating annotators' annotations

possible shemes:
    mean
    majority votes
"""

import sys

def mean(num_li):
    return float(sum(num_li)) / len(num_li)

def main():
    label_li = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        str_li = line.split()
        num_li = [float(e) for e in str_li]
        label = mean(num_li)
        label_li.append(label)

    for label in label_li:
        print label

if __name__ == "__main__":
    main()

