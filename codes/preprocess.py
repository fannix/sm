"""
Preprocess the data file

Convert the data file into tab separated file.
"""

import sys

def process(record_li):
    """
    Convert each record to a tab separted line

    record_li: list of record. Each record contains 6 lines
    """
    lines_per_record = 3
    num_record = len(record_li)/lines_per_record
    for i in range(num_record):
        a_record = record_li[i * lines_per_record: 
                             i * lines_per_record + lines_per_record]
        text = a_record[1]
        score = a_record[2]

        print "%s\t%s" % (text, score)


if __name__ == "__main__":
    record_li = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            record_li.append(line)

    process(record_li)
