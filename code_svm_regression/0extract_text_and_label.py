#encoding: utf-8
"""
Extract text and labels from the training and test set
"""
import sys
import os
import os.path
import re


def from_trainset1():
    datadir = "data_svm_regression/0trainset1/"

    #extract text
    text_li = []
    for fname in ["a1.txt", "a2.txt"]:
        f = open(os.path.join(datadir, fname))
        lineno = 1
        for line in f:
            line = line.strip()
            if not line:
                continue
            if lineno % 3 == 2:
                text_li.append(line)
            lineno += 1
        f.close()

    #extract labels
    label_li = []
    for annotator in ['a', 'b', 'c', 'e']:
        li = []
        for pattern in ["%s1.txt", "%s2.txt"]:
            fname = pattern % annotator
            f = open(os.path.join(datadir, fname))
            lineno = 1
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if lineno % 3 == 0:
                    li.append(line)
                lineno += 1
            f.close()
        label_li.append(li)

    return text_li, label_li


def from_trainset2():
    datadir = "data_svm_regression/0trainset2/"

    #extract text
    text_li = []
    retweet = False
    for fname in ["wb混合1A.txt", "wb混合2A.txt"]:
        f = open(os.path.join(datadir, fname))
        offset = 1
        for line in f:
            line = line.strip()
            if not line:
                continue
            if offset == 1:
                if line.decode("utf-8")[-2:] == u'原创':
                    retweet = False
                elif line.decode("utf-8")[-2:] == u'转发':
                    retweet = True

            if offset == 3:
                text_li.append(line)
            if retweet and offset == 4:
                text_li[-1] = text_li[-1] + " // " +  line
            if offset > 3 and line in ["-3", "-2", "-1", "0", "1", "2", "3"]:
                offset = 0
            offset += 1

        f.close()

    for fname in ["wb原创3A.txt"]:
        f = open(os.path.join(datadir, fname))
        lineno = 1
        for line in f:
            line = line.strip().decode("gb18030")
            if not line:
                continue
            if lineno % 3 == 2:
                text_li.append(line.encode("utf-8"))
            lineno += 1
        f.close()

    #extract labels
    label_li = []
    for annotator in "ABCDE":
        li = []
        for pattern in ["wb混合1%s.txt", "wb混合2%s.txt", "wb原创3%s.txt"]:
            fname = pattern % annotator
            f = open(os.path.join(datadir, fname))
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line in set(["-3", "-2", "-1", "0", "1", "2", "3"]):
                    li.append(line)

        label_li.append(li)

    return text_li, label_li


def from_testset():
    datadir = "data_svm_regression/0testset"
    dstdir = "data_svm_regression/1testset/"
    file_li = os.listdir(datadir)
    #file_li = ["1251648860.txt"]
    time_pattern = "created_at:(.+)"
    text_pattern = "^text:(.*)"
    retweet_pattern = "retweet_text:"

    for fname in file_li:
        if fname[-3:] != "txt":
            continue
        print fname,
        time_li = []
        text_li = []
        f = open(os.path.join(datadir, fname))
        for line in f:
            line = line.strip()
            time_matches = re.findall(time_pattern, line)
            text_matches = re.findall(text_pattern, line)
            if text_matches:
                    text = text_matches[0]
                    text_li.append(text.strip())
                    if len(text) < 1:
                        continue
            if time_matches:
                time = time_matches[0]
                time_li.append(time.strip())
            if retweet_pattern in line:
                retweet = line[len(retweet_pattern):]
                text_li[-1] = text_li[-1] + " // " + retweet

        f.close()

        dstfile = open(os.path.join(dstdir, fname), 'w')
        print len(text_li), len(time_li)
        for i, e in enumerate(time_li):
            dstfile.write("%s\t%s\n" % (time_li[i], text_li[i]))
        dstfile.close()



def main():
    #training set 1
    #text_li, label_li = from_trainset1()
    #f = open("data_svm_regression/1trainset/text1.txt", 'w')
    #f.write("\n".join(text_li))
    #f.close()
    #f = open("data_svm_regression/1trainset/label1.txt", 'w')
    #print len(label_li[0])
    #print len(text_li)
    #for i, e in enumerate(label_li[0]):
        #f.write("%s\t%s\t%s\t%s\n" % (label_li[0][i],
            #label_li[1][i], label_li[2][i], label_li[3][i]))
    #f.close()

    #training set 2
    #text_li, label_li = from_trainset2()
    #f = open("data_svm_regression/1trainset/text2.txt", 'w')
    #f.write("\n".join(text_li))
    #f.close()
    #f = open("data_svm_regression/1trainset/label2.txt", 'w')
    #print len(label_li)
    #print len(label_li[0])
    #print len(text_li)
    #for i, e in enumerate(label_li[0]):
        #f.write("%s\t%s\t%s\t%s\t%s\n" % (label_li[0][i],
            #label_li[1][i], label_li[2][i], label_li[3][i], label_li[4][i]))
    #f.close()

    #test set
    from_testset()

if __name__ == "__main__":
    main()
