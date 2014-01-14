'''
Shortest Non-Shared Substring Problem: Find the shortest substring of one string that does not appear in another string.
    Input: Strings Text1 and Text2.
    Output: The shortest substring of Text1 that does not appear in Text2.
'''
from FreqPattern import PatternGenerator, PatternInTree
from SuffixTree import BuildSuffixTree

def FindNonShared(string1, string2):
    suffixtree = BuildSuffixTree(string1 + "$")
    #print suffixtree
    for i in range(2, len(string2) + 1):
        existing = []
        for pattern in PatternGenerator(string2, i):
            if pattern in existing:
                continue
            else:
                existing.append(pattern)
            if not PatternInTree(pattern, suffixtree):
                return pattern

def test():
    print "winner:", FindNonShared("ABCD", "BCD")
    print "winner:", FindNonShared("TCGGTAGATTGCGCCCACTC",  "AGGGGCTCGCAGTGTAAGAA")

if __name__ == "__main__":
    '''
    test()
    '''
    infile   = "dataset_95_6.txt"
    #infile   = "tmp2"
    string1, string2 = [ x.strip() for x in open(infile).readlines()]
    print FindNonShared(string1, string2)
