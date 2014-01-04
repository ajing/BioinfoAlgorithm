'''
Implement LINEARSPACEALIGNMENT to solve the Global Alignment Problem for a large dataset.
    Input: Two long (10000 amino acid) protein strings written in the single-letter amino acid alphabet.
    Output: The maximum alignment score of these strings, followed by an alignment achieving this maximum score. Use the BLOSUM62 scoring matrix and indel penalty = 5.
'''

from MiddleEdge import GetMaxScore, MiddleEdge

def AddReference(node, reftop, refleft):
    return (node[0] + reftop, node[1] + refleft)

def MiddleEdgeMod(top, bottom, left, right, v, w):
    #print v[top:bottom], w[left:right]
    start, end = MiddleEdge(v[top:bottom], w[left:right])
    start = AddReference(start, top, left)
    end   = AddReference(end, top, left)
    return (start, end)

def EdgeDirect(edge):
    # up 1, left 2, diag 3
    start = edge[0]
    end   = edge[1]
    if start[0] == end[0]:
        # left
        return 2
    elif start[1] == end[1]:
        # down
        return 1
    else:
        # diag
        return 3

def PrintBacktrack(v, w, linklist):
    matchlist = []
    ijlist = [edge[0] for edge in linklist]
    ijlist.append(linklist[-1][1])
    #print ijlist
    old_i = 0
    old_j = 0
    for each in ijlist:
        i, j = each
        if i == (old_i + 1) and j == (old_j + 1):
            matchlist.append([v[i - 1], w[j - 1]])
        if i == old_i and j == (old_j + 1):
            matchlist.append(["-", w[j - 1]])
        if i == (old_i + 1) and j == old_j:
            matchlist.append([v[i - 1], "-"])
        old_i = i
        old_j = j
    firstline = []
    secondline = []
    for i in range(len(matchlist)):
        firstline.append(matchlist[i][0])
        secondline.append(matchlist[i][1])
    firststring  = "".join(firstline)
    secondstring = "".join(secondline)
    print firststring
    print secondstring

def LinearSpaceAlign(top, bottom, left, right, v, w):
    if left == right:
        return [((x, left), (x + 1, left)) for x in range(top, bottom)]
    elif top == bottom:
        return [((top, x), (top, x + 1)) for x in range(left, right)]
    else:
        middle = (left + right) / 2
        mid_edge = MiddleEdgeMod(top, bottom, left, right, v, w)
        mid_node = mid_edge[0][0]
        up_bottom = mid_node
        up_right  = middle
        # up 1, left 2, diag 3
        if EdgeDirect(mid_edge) == 2 or EdgeDirect(mid_edge) == 3:
            down_left = middle + 1
        else:
            down_left = middle
        if EdgeDirect(mid_edge) == 1 or EdgeDirect(mid_edge) == 3:
            down_top  = mid_node + 1
        else:
            down_top  = mid_node
        return LinearSpaceAlign(top, up_bottom, left, up_right, v, w) + [mid_edge] + LinearSpaceAlign(down_top, bottom, down_left, right, v, w)

def test():
    v = "PLEASANTLY"
    w = "MEANLY"
    #v = "PRTEINS"
    #w = "PRTWPSEIN"
    #v = "ACTTAATT"
    #w = "GAGCAATT"
    GetMaxScore(v, w)
    linklist = LinearSpaceAlign(0, len(v), 0, len(w), v, w)
    PrintBacktrack(v, w, linklist)

def main():
    infile  = "/home/ajing/Downloads/dataset_79_14.txt"
    #infile  = "tmp"
    v, w = [ x.strip() for x in open(infile).readlines() ]
    GetMaxScore(v, w)
    linklist = LinearSpaceAlign(0, len(v), 0, len(w), v, w)
    PrintBacktrack(v, w, linklist)

if __name__ == "__main__":
    #test()
    main()
