'''
   Solve the Global Alignment Problem.
   Input: Two protein strings written in the single-letter amino acid alphabet.
   Output: The maximum alignment score of these strings followed by an alignment achieving this maximum score. Use the BLOSUM62 scoring matrix and indel penalty 5
'''
import numpy as np

gap_score = 5
BLOSUM = "BLOSUM62.txt"

def ParseMatrix(infile):
    dmatrix = dict()
    flag  = 1  #first line flag
    i     = 0
    for line in open(infile):
        content = line.strip().split()
        if flag:
            colnames = content
            flag = 0
            continue
        rowname = colnames[i]
        for j in range(len(colnames)):
            dmatrix[rowname, colnames[j]] = int(content[j+1])
        i += 1
    return dmatrix

def MaxScore(v, w, i, j, score, dmatrix, backtrack):
    maxscore = -1000
    # v is gap
    newscore = score[i - 1, j]  - gap_score
    if newscore > maxscore:
        backtrack[i, j] = 1
        maxscore = newscore
    # w is gap
    newscore = score[i, j - 1]  - gap_score
    if newscore > maxscore:
        backtrack[i, j] = 2
        maxscore = newscore
    newscore = score[i - 1, j - 1] + dmatrix[v[i - 1], w[j - 1]]
    if newscore > maxscore:
        backtrack[i, j] = 3
        maxscore = newscore
    return maxscore

def ScoreInitialize(score):
    # add penalty score for each side
    rownum, colnum = score.shape
    for i in range(rownum):
        score[i, 0] = - i * gap_score
    for j in range(colnum):
        score[0, j] = - j * gap_score

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
    dmatrix = ParseMatrix(BLOSUM)
    for i in range(1, 1 + v_len):
        for j in range(1, 1 + w_len):
            score[i, j] = MaxScore(v, w, i, j, score, dmatrix, backtrack)
    print int(score[v_len, w_len])
    print score
    PrintBacktrack(backtrack, v, w)

if __name__ == "__main__":
    v = "PLEASANTLY"
    w = "MEASNLY"
    #v = "TNIYGLKERVPR"
    #w = "TNNMQTRMWCVLIAAPCHLW"
    #infile  = "/home/ajing/Downloads/dataset_76_3.txt"
    #v, w = [ x.strip() for x in open(infile).readlines() ]
    #print v
    #print w
    GlobalAlign(v, w)
