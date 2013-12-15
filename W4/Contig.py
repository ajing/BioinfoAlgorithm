'''
Contig Generation Problem: Generate the contigs from a collection of reads (with imperfect coverage).
     Input: A collection of k-mers Patterns.
     Output: All contigs in DeBruijn(Patterns).
'''

from DeBruijn import DeBruijnKmer
from collections import defaultdict

def GetInvertex(graph):
    invex  = defaultdict(list)
    for eachstart in graph:
        for eachend in graph[eachstart]:
            invex[eachend].append(eachstart)
    return invex

def GetChildPath(outvex, invex, vetex):
    # As the children can only have one outgoing and incomming edge, so I assume it will be easier to write a function here
    apath = []
    next_vetex = vetex
    while len(outvex[next_vetex]) == 1 and len(invex[next_vetex]) == 1:
        apath.append(next_vetex)
        next_vetex = outvex[next_vetex][0]
    apath.append(next_vetex)
    return apath

def Path2Contig(paths):
    contigs = []
    for apath in paths:
        contig = apath[0][:-1] + "".join([x[-1] for x in apath])
        contigs.append(contig)
    return contigs

def FindPathforVetex(outvex, invex, vetex):
    path = []
    contigs = []
    for each in outvex[vetex]:
        apath = GetChildPath(outvex, invex, each)
        path.append( [vetex] + apath)
    return path

def SelectVetex(outvex, invex):
    vexs   = list(set(outvex.keys() + invex.keys()))
    vexlist = []
    for eachvex in vexs:
        indegree  = len(invex[eachvex])
        outdegree = len(outvex[eachvex])
        if indegree != 1 or outdegree > 1:
            vexlist.append(eachvex)
    return vexlist

def Contig_main(seqs):
    outvex = DeBruijnKmer(seqs)
    invex  = GetInvertex(outvex)
    vexlist = SelectVetex(outvex, invex)
    contiglist = []
    for each in vexlist:
        path = FindPathforVetex(outvex, invex, each)
        contigs = Path2Contig(path)
        contiglist += contigs
    contiglist.sort()
    return contiglist


if __name__ == "__main__":
    #DeBruijn_main()
    infile  = "contig_generation_3.txt"
    infile  = "/home/ajing/Downloads/dataset_59_5.txt"
    seqs = [line.strip() for line in open(infile).readlines()]
    print "\n".join(Contig_main(seqs))
