'''
Shortest Non-Shared Substring Problem: Find the shortest substring of one string that does not appear in another string.
    Input: Strings Text1 and Text2.
    Output: The shortest substring of Text1 that does not appear in Text2.
'''
from FreqPattern import PatternGenerator, PatternInTree
from SuffixTree import BuildSuffixTree
import sys
sys.path.append("../W1")
from FrequentWord import PatternGenerator

def FindNonShared(string1, string2):
    suffixtree1 = BuildSuffixTree(string1 + "$")
    suffixtree2 = BuildSuffixTree(string2 + "$")
    #print suffixtree
    for i in range(2, len(string2) + 1):
        existing   = []
        for pattern in PatternGenerator( i):
            if not pattern in existing:
                existing.append(pattern)
            else:
                continue
            if PatternInTree(pattern, suffixtree1) and not PatternInTree(pattern, suffixtree2):
                return pattern

def test():
    print "winner:", FindNonShared("ABCD", "BCD")
    print "winner:", FindNonShared("TCGGTAGATTGCGCCCACTC",  "AGGGGCTCGCAGTGTAAGAA")
    print "winner:", FindNonShared("CCAAGCTGCTAGAGG",  "CATGCTGGGCTGGCT")

if __name__ == "__main__":
    '''
    test()
    '''
    infile   = "/home/ajing/Downloads/dataset_95_6.txt"
    #infile   = "tmp2"
    string1, string2 = [ x.strip() for x in open(infile).readlines()]
    print FindNonShared(string1, string2)
