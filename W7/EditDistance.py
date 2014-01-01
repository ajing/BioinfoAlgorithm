'''
Edit Distance Problem: Find the edit distance between two strings.
    Input: Two strings.
    Output: The edit distance between these strings.
'''
import numpy as np

gap_score = 1

def MinScore(v, w, i, j, score, backtrack):
    minscore = 10000000
    # v is gap
    newscore = score[i - 1, j]  + gap_score
    if newscore < minscore:
        backtrack[i, j] = 1
        minscore = newscore
    # w is gap
    newscore = score[i, j - 1]  + gap_score
    if newscore < minscore:
        backtrack[i, j] = 2
        minscore = newscore
    # match or mismatch
    if v[i - 1] == w[j - 1]:
        newscore = score[i - 1, j - 1]
    else:
        newscore = score[i - 1, j - 1] + 1
    if newscore < minscore:
        backtrack[i, j] = 3
        minscore = newscore
    return minscore

def ScoreInitialize(score):
    # add penalty score for each side
    rownum, colnum = score.shape
    for i in range(rownum):
        score[i, 0] = i * gap_score
    for j in range(colnum):
        score[0, j] = j * gap_score

def PrintBacktrack(backtrack, v, w):
    i = len(v)
    j = len(w)
    matchlist = []
    while i > 0 or j > 0:
        if backtrack[i, j] == 3:
            matchlist.append([v[i - 1], w[j - 1]])
            i -= 1
            j -= 1
        elif backtrack[i, j] == 2:
            matchlist.append(["-", w[j - 1]])
            j -= 1
        else:
            matchlist.append([v[i - 1], "-"])
            i -= 1
    matchlist.reverse()
    firstline = []
    secondline = []
    for i in range(len(matchlist)):
        firstline.append(matchlist[i][0])
        secondline.append(matchlist[i][1])
    print "".join(firstline)
    print "".join(secondline)


def GlobalAlign(v, w):
    # v and w are two sequences
    v_len = len(v)
    w_len = len(w)
    score = np.zeros([v_len + 1, w_len + 1])
    ScoreInitialize(score)
    # 1 is | (down); 2 is -> left; 3 is \ diag
    backtrack = np.zeros([v_len + 1, w_len + 1])
    for i in range(1, 1 + v_len):
        for j in range(1, 1 + w_len):
            score[i, j] = MinScore(v, w, i, j, score, backtrack)
    print int(score[v_len, w_len])
    print score
    PrintBacktrack(backtrack, v, w)

if __name__ == "__main__":
    v = "PLEASANTLY"
    w = "MEANLY"
    #v = "TNIYGLKERVPR"
    #w = "TNNMQTRMWCVLIAAPCHLW"
    infile  = "/home/ajing/Downloads/dataset_77_3.txt"
    #infile  = "tmp"
    v, w = [ x.strip() for x in open(infile).readlines() ]
    #print v
    #print w
    GlobalAlign(v, w)
