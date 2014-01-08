'''
Find the number of breakpoints in a permutation.
    Input: A permutation P.
    Output: The number of breakpoints in P.
'''

import numpy as np
from GreedySort import P

class P(P):
    def isinorder(self, alist):
        if alist[0] < 0:
            alist = - alist[::-1]
        if alist[0] == (alist[1] - 1):
            return True
        else:
            return False

    def numberbreakpoints(self):
        complete_list = np.append( self.p, len(self.p) + 1)
        complete_list = np.append( 0, complete_list)
        bp_num = 0
        for i in range(len(complete_list) - 1):
            if not self.isinorder(complete_list[i:(i+2)]):
                bp_num += 1
        return bp_num

def testP():
    newp = P([1,-2,3])
    print newp.numberbreakpoints()

if __name__ == "__main__":
    #testP()
    newp = "(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)"
    infile  = "tmp"
    infile  = "/home/ajing/Downloads/dataset_88_1.txt"
    newp = open(infile).readlines()[0].strip()
    newp = [int(x) for x in newp[1:-1].split()]
    newp = P(newp)
    print newp.numberbreakpoints()
