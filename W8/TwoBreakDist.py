'''
Solve the 2-Break Distance Problem.
    Input: Genomes P and Q.
    Output: The 2-break distance d(P, Q).
'''

from BreakPoints import P

def Blocks(P, Q):
    return len(P)

def FindEdgePop(edges, node):
    for eachedge in edges:
        if node == eachedge[0]:
            nextnode = eachedge[1]
            break
        elif node == eachedge[1]:
            nextnode = eachedge[0]
            break
    if 'nextnode' in locals():
        edges.remove(eachedge)
        return nextnode
    else:
        return False

def Cycle(Pedges, Qedges):
    pedges_cp = Pedges[:]
    qedges_cp = Qedges[:]
    circles = []
    while pedges_cp:
        startedge = pedges_cp.pop()
        circle = startedge
        nextnode = FindEdgePop(qedges_cp, startedge[1])
        circle.append(nextnode)
        while True:
            nextnode = FindEdgePop(pedges_cp, nextnode)
            if not nextnode:
                break
            else:
                circle.append(nextnode)
            nextnode = FindEdgePop(qedges_cp, nextnode)
            circle.append(nextnode)
        circles.append(circle[:-1])
    return len(circles)

def EdgesfromString(astring):
    edges  = []
    blocks = 0
    for each in astring.split(")")[:-1]:
        each  =  each[1:]
        alist = [int(x) for x in each.split()]
        newp  = P(alist)
        blocks += len(newp)
        edges  += newp.breakpointedges()
    return edges, blocks

def Dist(pstring, qstring):
    blocks = 0
    cycles = 0
    edgesp, blocksp = EdgesfromString(pstring)
    edgesq, blocksq = EdgesfromString(qstring)
    if blocksp != blocksq:
        raise Exception("blocks are not equal:p:" + p + "q:" + q)
    return blocksp - Cycle(edgesp, edgesq)

def test(p, q):
    print Cycle(p, q)


if __name__ == "__main__":
    pstring = "(+1 +2 +3 +4 +5 +6)"
    qstring = "(+1 -3 -6 -5)(+2 -4)"
    infile  = "tmp"
    infile  = "/home/ajing/Downloads/dataset_89_1.txt"
    pstring, qstring = [x.strip() for x in open(infile).readlines()]
    print Dist(pstring, qstring)
