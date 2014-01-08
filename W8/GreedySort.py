'''
Implement GREEDYSORTING.
    Input: A permutation P.
    Output: The sequence of permutations corresponding to applying GREEDYSORTING to P, ending with the identity permutation.
'''
import numpy as np

class P:
    def __init__(self, alist):
        # a list is a numeric list
        self.p = np.array(alist)

    def __str__(self):
        astrlist = []
        for each in self.p:
            if each > 0:
                astrlist.append("+" + str(each))
            else:
                astrlist.append(str(each))
        return "(" + " ".join(astrlist) + ")"

    def __len__(self):
        return len(self.p)

    def kissorted(self, k):
        return self.p[k - 1] == k

    def kthelement(self, k):
        return self.p[k - 1]

    def ksort(self, k):
        kindex = np.where(abs(self.p) == k)[0]
        self.reverse(k, kindex + 1)

    def reverse(self, i, j):
        if i > j:
            raise Exception("i cannot be larger than j")
        elif i == j:
            self.p[i - 1] = -self.p[i - 1]
        else:
            self.p[(i - 1) : j] = -self.p[(i - 1) : j][::-1]

    def breakpointedges(self):
        edges = []
        for i in range(len(self.p) - 1):
            pair = self.p[i:(i + 2)]
            edges.append([pair[0], -pair[1]])
        edges.append([self.p[-1], -self.p[0]])
        return edges

def testP():
    newp = P([1,-2,3])
    print newp
    newp.reverse(1,2)
    print newp

def GreedySort(inputP):
    appReversalDist = 0
    for k in range(1, len(inputP) + 1):
        if not inputP.kissorted(k):
            inputP.ksort(k)
            appReversalDist += 1
            print inputP
        if inputP.kthelement(k) == -k:
            inputP.reverse(k, k)
            appReversalDist += 1
            print inputP
    return appReversalDist

if __name__ == "__main__":
    #testP()
    newp = "(-3 +4 +1 +5 -2)"
    infile  = "tmp"
    infile  = "/home/ajing/Downloads/dataset_87_2.txt"
    newp = open(infile).readlines()[0].strip()
    newp = [int(x) for x in newp[1:-1].split()]
    newp = P(newp)
    GreedySort(newp)
