'''
Solve the Local Alignment Problem.
    Input: Two protein strings written in the single-letter amino acid alphabet.
    Output: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty 5
'''

from GlobalAlign import *

PAM = "PAM250_1.txt"

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
    if maxscore < 0:
        maxscore = 0
        backtrack[i, j] = 4
    return maxscore

def PrintBacktrack(score, backtrack, v, w):
    matchlist = []
    i, j = np.unravel_index(score.argmax(), score.shape)
    while (i > 0 or j > 0) and score[i, j] > 0:
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

def LocalAlign(v, w):
    # v and w are two sequences
    v_len = len(v)
    w_len = len(w)
    score = np.zeros([v_len + 1, w_len + 1])
    # 1 is | (down); 2 is -> left; 3 is \ diag
    backtrack = np.zeros([v_len + 1, w_len + 1])
    dmatrix = ParseMatrix(PAM)
    for i in range(1, 1 + v_len):
        for j in range(1, 1 + w_len):
            score[i, j] = MaxScore(v, w, i, j, score, dmatrix, backtrack)
    print int(np.amax(score))
    PrintBacktrack(score, backtrack, v, w)


if __name__ == "__main__":
    w = "PENALTY"
    v = "MEANLY"
    #v = "GCCGCCGTCGTTTTCAGCAGTTATGTCAGAT"
    #w = "GCCCAGTTATGTCAGGGGGCACGAGCATGCACA"
    #v  = "VPYRVWGCCPMGCLHMGEDSHAETAAFCVAWDCTSICKTTYSTTRYSGAGLAMLYMRWSFDPDWAGSHFWMFCQVDRYMHNQYNLSCSDHMYRNHCDPAIQDVGRTLK"
    #w  = "QKEVFEHHAYHNVSNIMYMLFTAFPRRCNLFSNWRIDYPENDRERRLGTFFESWREFDRQYKNWIMLNMVWYAKWQSHYKPGQQDCGITMNV"
    infile  = "/home/ajing/Downloads/dataset_76_9.txt"
    v, w = [ x.strip() for x in open(infile).readlines() ]
    LocalAlign(v, w)
