'''
Solve the Overlap Alignment Problem.
    Input: Two strings v and w, each of length at most 1000.
    Output: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v' of v and a prefix w of w achieving this maximum score. Use an alignment score in which matches count +1 and both the mismatch and indel penalties are 2.
'''

import numpy as np

gap_score = 2

def MaxScore(v, w, i, j, score, backtrack):
    maxscore = -10000
    # match or mismatch
    if v[i - 1] == w[j - 1]:
        newscore = score[i - 1, j - 1] + 1
    else:
        newscore = score[i - 1, j - 1] - 2
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

def FindMaximunColumn(score):
    indexlist = np.where(score[-1, :] == np.amax(score[-1, :]))
    return indexlist[0][0]

def PrintBacktrack( score, backtrack, v, w):
    i = len(v)
    j = FindMaximunColumn(score)
    #print "j", j
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
    print firststring
    print secondstring


def LocalAlign(v, w):
    # v and w are two sequences
    v_len = len(v)
    w_len = len(w)
    score = np.zeros([v_len + 1, w_len + 1])
    # 1 is | (down); 2 is -> left; 3 is \ diag
    backtrack = np.zeros([v_len + 1, w_len + 1])
    for i in range(1, 1 + v_len):
        for j in range(1, 1 + w_len):
            score[i, j] = MaxScore(v, w, i, j, score, backtrack)
    print int(np.amax(score[-1, :]))
    #print score
    #print score[:,-1]
    PrintBacktrack( score, backtrack, v, w)

if __name__ == "__main__":
    v = "PAWHEAE"
    w = "HEAGAWGHEE"
    infile  = "/home/ajing/Downloads/dataset_77_7.txt"
    #infile  = "tmp"
    v, w = [ x.strip() for x in open(infile).readlines() ]
    #print v
    #print w
    LocalAlign(v, w)
