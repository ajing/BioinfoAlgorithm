"""
    Input: An integer k.
    Output: A k-universal circular string.
"""

from DeBruijn import DeBruijnKmer
from EulerianCyc import EulerianCyc
from EulerianPath import JoinPathtoString
import sys

def StringsGen(N):
    s_list = []
    for i in range(2**N):
        binary = bin(i)
        s_list.append(str(binary)[2:].zfill(N))
    return s_list


if __name__ == "__main__":
    num   = int(sys.argv[1])
    print num
    seqs  = StringsGen(num)
    graph = DeBruijnKmer(seqs)
    print graph
    circle = EulerianCyc(graph)
    pathlist = [x[-1] for x in circle]
    print "".join(pathlist)
