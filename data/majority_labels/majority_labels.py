"""
Output the majority labels and evaluate the agreement
"""
import sys
from collections import defaultdict

def output_majority(line_li):
    """
    Output majority labels

    line_li: a line for a sample's all labels
    """
    no_majority_label_li = []
    for i, line in enumerate(line_li):
        count = defaultdict(lambda: 0)
        label_li = line.split()
        n_label = len(label_li)
        for e in label_li:
            count[e] += 1

        max_n = 0
        max_symbol = ""
        for e in count:
            if count[e] > max_n:
                max_n = count[e]
                max_symbol = e

        if max_n > n_label/2:
            print max_symbol
        else:
            print max_symbol
            no_majority_label_li.append(i+1)

    print >> sys.stderr, no_majority_label_li, len(no_majority_label_li)


if __name__ == "__main__":
    line_li = []
    for line in sys.stdin:
        line_li.append(line.strip())
    output_majority(line_li)
