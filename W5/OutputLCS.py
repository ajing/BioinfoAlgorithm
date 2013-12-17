'''
Longest common subsequence problem
Use OUTPUTLCS (reproduced below) to solve the Longest Common Subsequence Problem.
     Input: Two strings s and t.
     Output: A longest common subsequence of s and t.
'''

import numpy as np
import sys
sys.setrecursionlimit(2000)

def LCS(v, w):
    # v and w are two sequences
    v_len = len(v)
    w_len = len(w)
    score = np.zeros([v_len + 1, w_len + 1])
    # 1 is | (down); 2 is -> left; 3 is \ diag
    backtrack = np.zeros([v_len + 1, w_len + 1])
    for i in range(1, 1 + v_len):
        for j in range(1, 1 + w_len):
            if v[i - 1] == w[j - 1]:
                score[i,j] = max(score[i - 1, j], score[i, j - 1], score[i - 1, j - 1] + 1)
            else:
                score[i,j] = max(score[i - 1, j], score[i, j - 1])
            if score[i, j] == score[i - 1, j]:
                backtrack[i,j] = 1
            elif score[i, j] == score[i, j - 1]:
                backtrack[i,j] = 2
            else:
                backtrack[i,j] = 3
    #print score
    #print backtrack
    return score[v_len - 1, w_len - 1], backtrack

def OutputLCS(backtrack, v, i, j, finallist):
    if i == 0 or j == 0:
        return
    if backtrack[i,j] == 1:
        OutputLCS(backtrack, v, i - 1, j, finalstring)
    elif backtrack[i,j] == 2:
        OutputLCS(backtrack, v, i, j - 1, finalstring)
    else:
        OutputLCS(backtrack, v, i - 1, j - 1, finalstring.append(v[i - 1]))

if __name__ == "__main__":
    infile = "tmp2"
    infile  = "/home/ajing/Downloads/dataset_74_5.txt"
    v, w = [ x.strip() for x in open(infile).readlines() ]
    score, backtrack = LCS(v,w)
    finalstring = []
    OutputLCS(backtrack, v, len(v) - 1, len(w) - 1, finalstring)
    finalstring.reverse()
    print "".join(finalstring)
