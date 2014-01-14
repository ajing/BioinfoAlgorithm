'''
## This file is obsolete because too slow. The FreqPattern part has become a part of SuffixTree file
'''
# matchedge has been modified!!!!!!!!!!!!!1
from SuffixTree import BuildSuffixTree, MatchEdge, IndexSame

def PatternInTree(pattern, stree):
    startnode = 1
    while pattern:
        matched_s = MatchEdge(pattern, stree, startnode)
        if matched_s:
            index   = IndexSame(matched_s, pattern)
            pattern = pattern[index:]
            startnode, index = stree[startnode][matched_s]
        else:
            for key in stree[startnode]:
                if key.startswith(pattern):
                    return True
            return False
    return True

def PatternGenerator(text, n):
    for i in range(len(text) - n + 1):
        yield text[i:n + i]

def FreqPatternExist(text, n):
    patterns = [ text[i:n + i] for i in range(len(text) - n + 1) ]
    for pattern in patterns:
        if patterns.count(pattern) > 1:
            return pattern
    return False

def FreqPattern(text):
    suffixtree = BuildSuffixTree(text)
    print suffixtree
    startlen   = len(text) * 2/5
    for i in range(startlen, len(text)):
        for pattern in PatternGenerator(text[:-1], i):
            print pattern
            if PatternInTree(pattern, suffixtree):
                bestp = pattern
    return bestp

def FreqCheat(text):
    bestp = ""
    startlen   = len(text) * 2/5
    for i in range(startlen, len(text)):
        pattern = FreqPatternExist(text, i)
        if pattern:
            bestp = pattern
    return bestp

def test():
    print list(PatternGenerator("ABCD", 1))
    print list(PatternGenerator("ABCD", 2))
    stree = BuildSuffixTree("ABCDD$")
    assert(PatternInTree("ABC", stree))
    assert(PatternInTree("CA", stree) == False)
    assert(PatternInTree("ABD", stree) == False)
    print FreqPattern("ABCDBCD$")
    print FreqCheat("ABCDBCD$")
    print FreqCheat("AAA$")

if __name__ == "__main__":
    #test()
    infile   = "tmp"
    text = open(infile).readlines()[0].strip()
    print FreqCheat(text)
