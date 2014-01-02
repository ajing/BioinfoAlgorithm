'''
Solve the Alignment with Affine Gap Penalties Problem.
    Input: Two amino acid strings v and w (each of length at most 100).
    Output: The maximum alignment score between v and w, followed by an alignment of v and w achieving this maximum score. Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, and a gap extension penalty of 1.
'''
import numpy as np

BLOSUM = "BLOSUM62.txt"
epsilon = 1
thelta  = 11

def MaxScore(v, w, i, j, lower, middle, upper, backtrack, dmatrix):
    # for lower
    fromlower  = lower[i - 1, j] - epsilon
    frommiddle = middle[i - 1, j] - thelta
    if fromlower > frommiddle:
        lower[i, j] = fromlower
        backtrack[("lower", i, j)] = ("lower", i - 1, j)
    else:
        lower[i, j] = frommiddle
        backtrack[("lower", i, j)] = ("middle", i - 1, j)
    # for upper
    fromupper = upper[i, j - 1] - epsilon
    frommiddle = middle[i, j - 1] - thelta
    if fromupper > frommiddle:
        upper[i, j] = fromupper
        backtrack[("upper", i, j)] = ("upper", i, j - 1)
    else:
        upper[i, j] = frommiddle
        backtrack[("upper", i, j)] = ("middle", i, j - 1)
    # for middle
    frommiddle = middle[i - 1, j - 1] + dmatrix[v[i - 1], w[j - 1]]
    middle[i, j] = max(lower[i, j], frommiddle, upper[i, j])
    if middle[i, j] == frommiddle:
        backtrack[("middle", i, j)] = ("middle", i - 1, j - 1)
    elif middle[i, j] == lower[i, j]:
        backtrack[("middle", i, j)] = ("lower", i, j)
    else:
        backtrack[("middle", i, j)] = ("upper", i, j)

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

def PrintBacktrack(backtrack, v, w):
    i = len(v)
    j = len(w)
    matchlist = []
    nextnode = ("middle", i, j)
    while True:
        print nextnode
        if nextnode[0] == "upper":
            matchlist.append(["-", w[j - 1]])
        elif nextnode[0] == "lower":
            matchlist.append([v[i - 1], "-"])
        else:
            matchlist.append([v[i - 1], w[j - 1]])
        nextnode = backtrack[nextnode]
        i = nextnode[1]
        j = nextnode[2]
        if i == 0 and j == 0:
            break
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

def ScoreInitialize(upper, middle, lower):
    # for middle
    rownum, colnum = middle.shape
    for i in range(1, rownum):
        middle[i, 0] = - thelta - (i - 1) * epsilon
    for j in range(1, colnum):
        middle[0, j] = - thelta - (j - 1) * epsilon
    # for lower
    for i in range(1, rownum):
        lower[i, 0] = - thelta - (i - 1) * epsilon
    for j in range(colnum):
        lower[0, j] = - np.inf
    # for upper
    for i in range(rownum):
        upper[i, 0] = - np.inf
    for j in range(1, colnum):
        upper[0, j] = - thelta - (j - 1) * epsilon


def AffineGap(v, w):
    # v and w are two sequences
    v_len = len(v)
    w_len = len(w)
    # lower is | (down); upper is -> left; middle is \ diag
    upper  = np.zeros([v_len + 1, w_len + 1])
    middle = np.zeros([v_len + 1, w_len + 1])
    lower  = np.zeros([v_len + 1, w_len + 1])
    ScoreInitialize(upper, middle, lower)
    backtrack = dict()
    dmatrix = ParseMatrix(BLOSUM)
    for i in range(1, 1 + v_len):
        for j in range(1, 1 + w_len):
            MaxScore(v, w, i, j, lower, middle, upper, backtrack, dmatrix)
    print "middle", middle
    print "lower", lower
    print "upper", upper
    print int(np.amax(middle))
    #print score
    #print score[:,-1]
    PrintBacktrack(backtrack, v, w)

if __name__ == "__main__":
    v = "PRTEINS"
    w = "PRTWPSEIN"
    AffineGap(v, w)
