"""Aggreating the emotion score from original, retweet, and the first retweet
"""

if __name__ == "__main__":
    import sys
    original = open(sys.argv[1]).readlines()
    retweet = open(sys.argv[2]).readlines()
    idx = open(sys.argv[3]).readlines()

    idx2score = {}

    assert len(original) == len(retweet) and len(original) == len(idx)
    for i in xrange(len(idx)):
        original_score = float(original[i].strip())
        retweet_score = float(retweet[i].strip())
        original_id, retweet_id = idx[i].strip().split()
        idx2score[original_id] = original_score + 0.5 * retweet_score

    for e in idx:
        original_id, retweet_id = e.strip().split()
        if retweet_id == "0":
            continue

        if retweet_id in idx2score:
            idx2score[original_id] +=  0.3 * idx2score[retweet_id]

    for e in idx2score:
        print e + "\t" + str(idx2score[e])
