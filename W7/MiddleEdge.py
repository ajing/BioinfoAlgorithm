'''
Solve the Middle Edge in Linear Space Problem (for protein strings). Use the BLOSUM62 scoring matrix and a linear indel penalty equal to 5.
    Input: Two amino acid strings.
    Output: A middle edge in the alignment graph in the form (i, j) (k, l), where (i, j) connects to (k, l). To compute scores, use the BLOSUM62 scoring matrix and a (linear) indel penalty equal to 5.
'''
import numpy as np
from AffineGap import ParseMatrix

BLOSUM = "BLOSUM62.txt"
gap_score = 5
dmatrix = ParseMatrix(BLOSUM)

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
    return two_column_score[:,1], backtrack

def GetMaxScore(v, w):
    w_len = len(w)
    fromsource, backtrack = LastColumnScore(v, w[:w_len/2], dmatrix)
    tosink, backtrack = LastColumnScore(v[::-1], w[w_len/2:][::-1], dmatrix)
    tosink = tosink[::-1]
    length = fromsource + tosink
    print int(max(length))

def MiddleEdge(v, w):
    w_len = len(w)
    v_len = len(v)
    fromsource, backtrack = LastColumnScore(v, w[:w_len/2], dmatrix)
    tosink, backtrack = LastColumnScore(v[::-1], w[w_len/2:][::-1], dmatrix)
    tosink = tosink[::-1]
    backtrack = backtrack[::-1]
    length = fromsource + tosink
    middle_start_x = w_len/2
    middle_start_y = length.argmax(axis = 0)
    middle_end_x   = w_len - backtrack[middle_start_y][1]
    middle_end_y   = v_len - backtrack[middle_start_y][0]
    return (middle_start_y, middle_start_x), (middle_end_y, middle_end_x)

def test():
    v = "PLEASANTLY"
    w = "MEASNLY"
    w_len = len(w)
    dmatrix = ParseMatrix(BLOSUM)
    sourceright = [-15., -11.,  -7.,  -3.,   6.,   1.,  -4.,  -9., -14., -19., -24.]
    tosinkright = [ -9.,  -4.,   1.,   6.,  11.,  13.,  12.,   7.,   1.,  -8., -20.]
    fromsource, backtrack = LastColumnScore(v, w[:w_len/2], dmatrix)
    tosink, backtrack = LastColumnScore(v[::-1], w[w_len/2:][::-1], dmatrix)
    tosink = tosink[::-1]
    assert(all(fromsource == sourceright))
    assert(all(tosink == tosinkright))
    print MiddleEdge(v, w)

def main():
    infile  = "tmp"
    infile  = "/home/ajing/Downloads/dataset_79_12.txt"
    v, w = [ x.strip() for x in open(infile).readlines() ]
    '''
    v = "PLEASANTLY"
    w = "MEASNLY"
    '''
    MiddleEdge(v, w)

if __name__ == "__main__":
    test()
