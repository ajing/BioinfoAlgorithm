'''
Solve the Fitting Alignment Problem.
    Input: Two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
    Output: A highest-scoring fitting alignment between v and w. Use the simple scoring method in which matches count +1 and both the mismatch and indel penalties are 1.
'''

import numpy as np

gap_score = 1

def MaxScore(v, w, i, j, score, backtrack):
    maxscore = -10000
    # match or mismatch
    if v[i - 1] == w[j - 1]:
        newscore = score[i - 1, j - 1] + 1
    else:
        newscore = score[i - 1, j - 1] - 1
    if newscore > maxscore:
        backtrack[i, j] = 3
        maxscore = newscore
    # w is gap
    newscore = score[i, j - 1]  - gap_score
    if newscore > maxscore:
        backtrack[i, j] = 2
        maxscore = newscore
    # v is gap
    newscore = score[i - 1, j]  - gap_score
    if newscore > maxscore:
        backtrack[i, j] = 1
        maxscore = newscore
    return maxscore

def ScoreInitialize(score):
    # add penalty score for each side
    rownum, colnum = score.shape
    for j in range(colnum):
        score[0, j] = - j * gap_score

def FindMaximunRow(score):
    indexlist = np.where(score[:,-1] == score[-1,-1])
    return indexlist[0][0]

def PrintBacktrack( score, backtrack, v, w):
    i = FindMaximunRow(score)
    j = len(w)
    matchlist = []
    # first w
    while j > 0:
        if backtrack[i, j] == 1:
            # up
            matchlist.append([v[i - 1], "-"])
            i -= 1
        elif backtrack[i, j] == 2:
            # left
            matchlist.append(["-", w[j - 1]])
            j -= 1
        else:
            # diagnal
            matchlist.append([v[i - 1], w[j - 1]])
            i -= 1
            j -= 1
    matchlist.reverse()
    firstline = []
    secondline = []
    for i in range(len(matchlist)):
        firstline.append(matchlist[i][0])
        secondline.append(matchlist[i][1])
    firststring  = "".join(firstline)
    secondstring = "".join(secondline)
    leftindex   = secondstring.index(w[0])
    rightindex  = secondstring.rindex(w[-1]) + 1
    print firststring[leftindex:rightindex]
    print secondstring[leftindex:rightindex]


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
            score[i, j] = MaxScore(v, w, i, j, score, backtrack)
    print int(np.amax(score[:,-1]))
    #print score
    PrintBacktrack( score, backtrack, v, w)

if __name__ == "__main__":
    v = "GTAGGCTTAAGGTTA"
    w = "TAGATA"
    v = "AAATTTAAA"
    w = "TATA"
    #v = "AAAAAAAAAAAATTATAA"
    #w = "TTT"
    infile  = "/home/ajing/Downloads/dataset_77_5.txt"
    #infile  = "tmp"
    v, w = [ x.strip() for x in open(infile).readlines() ]
    #print v
    #print w
    GlobalAlign(v, w)
