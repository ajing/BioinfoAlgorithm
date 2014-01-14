'''
Shortest Non-Shared Substring Problem: Find the shortest substring of one string that does not appear in another string.
    Input: Strings Text1 and Text2.
    Output: The shortest substring of Text1 that does not appear in Text2.
'''
from FreqPattern import PatternGenerator, PatternInTree
from SuffixTree import BuildSuffixTree

def FindNonShared(string1, string2):
    suffixtree = BuildSuffixTree(string1 + "$")
    print suffixtree
    #print suffixtree
    for i in range(2, len(string2) + 1):
        for pattern in PatternGenerator(string2, i):
            print pattern
            if not PatternInTree(pattern, suffixtree):
                print "winp:", pattern
                return pattern

def test():
    print "winner:", FindNonShared("ABCD", "BCD")
    print "winner:", FindNonShared("TCGGTAGATTGCGCCCACTC",  "AGGGGCTCGCAGTGTAAGAA")

if __name__ == "__main__":
    test()
    '''
    infile   = "/home/ajing/Downloads/dataset_95_5.txt"
    #infile   = "tmp2"
    string1, string2 = [ x.strip() for x in open(infile).readlines()]
    FindSharedSubstring(string1, string2)
    '''
