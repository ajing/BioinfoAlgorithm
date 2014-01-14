'''
Longest Shared Substring Problem: Find the longest Substring shared by two strings.
    Input: Strings Text1 and Text2.
    Output: The longest substring that occurs in both Text1 and Text2.
'''

#from SuffixTree import FindCommonPrefix, CurrentID, FindSimilarEdge, IndexSame
from SuffixTree import BuildSuffixTree, FindCommonPrefix, FindSimilarEdge, IndexSame

def LongestSimilarString(pattern, stree):
    pattern_left, startnode = FindCommonPrefix(pattern, stree)
    edge_sim = FindSimilarEdge(stree[startnode], pattern_left)
    index = IndexSame(pattern_left, edge_sim)
    node_len = len(pattern) - len(pattern_left) + index
    return pattern[:node_len]

def FindSharedSubstring(string1, string2):
    suffixtree = BuildSuffixTree(string1 + "$")
    #print suffixtree
    patterns   = [ string2[i:] for i in range(len(string2))]
    max_len    = 0
    max_string = ""
    for pattern in patterns:
        long_string = LongestSimilarString(pattern, suffixtree)
        long_len    = len(long_string)
        if long_len >= max_len:
            max_len = long_len
            max_string = long_string
    print max_string


def test():
    FindSharedSubstring("ABCD", "BCD")
    FindSharedSubstring("TCGGTAGATTGCGCCCACTC",  "AGGGGCTCGCAGTGTAAGAA")

if __name__ == "__main__":
    #test()
    infile   = "/home/ajing/Downloads/dataset_95_5.txt"
    #infile   = "tmp2"
    string1, string2 = [ x.strip() for x in open(infile).readlines()]
    FindSharedSubstring(string1, string2)
