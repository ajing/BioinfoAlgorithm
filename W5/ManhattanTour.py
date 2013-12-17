'''
    Dynamic programming for Manhattan Tourist Problem
    Input: Integers n and m, followed by an n * (m + 1) matrix down and an (n + 1) * m matrix right. The two matrices are separated by the - symbol.
    Output: The length of a longest path from source (0, 0) to sink (n, m) in the n * m rectangular grid whose edges are defined by the matrices down and right.
'''

import numpy as np

def ParseFile(infile):
    content = [x.strip() for x in open(infile).readlines()]
    n = int(content[0].strip())
    m = int(content[1].strip())
    index = content.index("-")
    down  = content[2:index]
    downmatrix = np.matrix(";".join(down))
    right = content[index + 1:]
    rightmatrix = np.matrix(";".join(right))
    return n, m, downmatrix, rightmatrix

def ManhattanTour(n, m, down, right):
    score = np.zeros([n+1, m+1])
    for i in range(1, n+1):
        score[i, 0] = score[i-1, 0] + down[i - 1, 0]
    for j in range(1, m+1):
        score[0, j] = score[0, j-1] + right[0, j - 1]
    for i in range(1, n+1):
        for j in range(1, m +1):
            score[i, j] = max(score[i - 1, j] + down[i - 1, j], score[i, j - 1] + right[i, j - 1])
    return score[n, m]


if __name__ == "__main__":
    infile = "tmp"
    infile  = "/home/ajing/Downloads/dataset_72_9.txt"
    n, m, dmatrix, rmatrix = ParseFile(infile)
    print ManhattanTour(n, m, dmatrix, rmatrix)
