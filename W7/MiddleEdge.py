'''
Solve the Middle Edge in Linear Space Problem (for protein strings). Use the BLOSUM62 scoring matrix and a linear indel penalty equal to 5.
    Input: Two amino acid strings.
    Output: A middle edge in the alignment graph in the form (i, j) (k, l), where (i, j) connects to (k, l). To compute scores, use the BLOSUM62 scoring matrix and a (linear) indel penalty equal to 5.
'''
import numpy as np
from AffineGap import ParseMatrix

BLOSUM = "BLOSUM62.txt"
gap_score = 5

def LastColumnScore(v, w, dmatrix):
    v_len = len(v)
    w_len = len(w)
    backtrack = [ -1 ] * (v_len + 1)
    two_column_score = np.zeros([v_len + 1, 2])
    for i in range(v_len + 1):
        two_column_score[i, 0] = - i * gap_score
    for j in range(1, w_len + 1):
        two_column_score[0, 1] = two_column_score[0, 0] - gap_score
        backtrack[0] = (0, j - 1)
        for i in range(1, v_len + 1):
            # list in the order of up left diag
            pre_values = [two_column_score[i - 1, 1] - gap_score, two_column_score[i, 0] - gap_score, two_column_score[i - 1, 0] + dmatrix[v[i - 1], w[j - 1]]]
            two_column_score[i, 1] = max(pre_values)
            index = pre_values.index(max(pre_values))
            # previous position in the order of up left diag
            pre_pos = [(i - 1, j), (i, j - 1), (i - 1, j - 1)]
            backtrack[i] = pre_pos[index]
        # renew column 0
        for i in range(v_len + 1):
            two_column_score[i, 0] = two_column_score[i, 1]
    return two_column_score, backtrack

def MiddleEdge(v, w):
    dmatrix = ParseMatrix(BLOSUM)
    w_len = len(w)
    fromsource, backtrack = LastColumnScore(v, w[:w_len/2], dmatrix)
    print "fromsource", fromsource
    tosink, backtrack = LastColumnScore(v[::-1], w[w_len/2::-1], dmatrix)
    tosink = tosink[::-1]
    print "tosink", tosink
    length = fromsource + tosink
    print "length", length
    middle_start_x = w_len/2
    middle_start_y = length.argmax(axis = 0)
    print middle_start_y
    middle_end_x   = middle_start_x + 1
    middle_end_y   = backtrack[middle_start_y]
    print (middle_start_x, middle_start_y), (middle_end_x, middle_end_y)

def test():
    v = "PLEASANTLY"
    w = "MEASNLY"
    dmatrix = ParseMatrix(BLOSUM)
    LastColumnScore(v, w, dmatrix)
    MiddleEdge(v, w)

if __name__ == "__main__":
    test()
    '''
    v = "PLEASANTLY"
    w = "MEASNLY"
    MiddleEdge(v, w)
    '''
