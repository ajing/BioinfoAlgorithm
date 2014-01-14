'''
Solve the Suffix Tree Construction Problem.
    Input: A string Text.
    Output: The edge labels of SuffixTree(Text). You may return these strings in any order.
'''

def IndexSame(string1, string2):
    min_s = min(len(string1), len(string2))
    if string1.startswith(string2) or string2.startswith(string1):
        return min_s
    for i in range(min_s):
        if string1[i] != string2[i]:
            return i

def MatchEdge( eachc, suffixtree, startnode):
    for eachkey in suffixtree[startnode]:
        if eachc.startswith(eachkey):
            return eachkey

def CurrentID():
    CurrentID.ID += 1
    return CurrentID.ID

def FindCommonPrefix(pattern, stree):
    original  = pattern
    startnode = 1
    matched_s = False
    while pattern:
        matched_s = MatchEdge(pattern, stree, startnode)
        if matched_s:
            index   = len(matched_s)
            pattern = pattern[index:]
            startnode, index = stree[startnode][matched_s]
        else:
            return pattern, startnode
    #print "original:", original
    #print "previous:", pattern_old, startold, matched_old
    #print "after:", pattern, startnode, matched_s
    return pattern, startnode

def FindSimilarEdge(branch, pattern):
    max_edge = ""
    max_len    = 0
    for eachedge in branch:
        i = IndexSame(eachedge, pattern)
        if i > max_len:
            max_edge = eachedge
            max_len  = i
    return max_edge

def ExtendSuffixTree(pattern_left, stree, matchnode, i, pattern):
    # static variable
    branch = stree[matchnode]
    ematched = FindSimilarEdge(branch, pattern_left)
    p_len = len(pattern)
    if ematched:
        # two new nodes with two new edges and one modified edge
        index = IndexSame(pattern_left, ematched)
        new_v = CurrentID()
        stree.append({})
        new_w = CurrentID()
        stree.append({"!":i})
        #print "branch", branch
        branch[ematched[:index]] = [ new_v, i ]
        node_len = p_len - len(pattern_left) + index
        if node_len > ExtendSuffixTree.maxshared:
            ExtendSuffixTree.maxshared = node_len
            ExtendSuffixTree.maxpattern = pattern[:node_len]
        stree[new_v][ematched[index:]] = branch[ematched]
        stree[new_v][pattern_left[index:]] = [ new_w, i]
        del branch[ematched]
        #print "branch after", branch
    else:
        new_v = CurrentID()
        stree.append({"!":i})
        branch[pattern_left] = [ new_v, i]

def PrintSuffix(suffixtree):
    edge_list = []
    for eachnode in suffixtree:
        edges = [x for x in eachnode.keys() if x != "!"]
        edge_list += edges
    print "\n".join(edge_list)

def BuildSuffixTree(text):
    # initialize the first id
    CurrentID.ID = 1
    ExtendSuffixTree.maxshared = 0
    ExtendSuffixTree.maxpattern = ""
    # suffix tree is like [0, {"CTG":(nextnode, startindex), "A"}, {}]
    patterns = [text[i:] for i in range(len(text))]
    suffixtree = [{},{}]
    for i in range(len(patterns)):
        eachp  = patterns[i]
        #print "eachp:", eachp
        patternleft, nodematched = FindCommonPrefix(eachp, suffixtree)
        #print patternleft, nodematched
        ExtendSuffixTree( patternleft, suffixtree, nodematched, i, eachp)
        #print "suffixtree:", suffixtree
    return suffixtree

def test():
    #suftree = BuildSuffixTree("ATAAA$")
    #print suftree
    #PrintSuffix(suftree)
    #print IndexSame("A", "AA")
    suftree = BuildSuffixTree("ABCDBCD$")
    print "maxpattern:", ExtendSuffixTree.maxpattern
    #PrintSuffix(suftree)
    suftree = BuildSuffixTree("ABCABAB$")
    print "maxpattern:", ExtendSuffixTree.maxpattern
    suftree = BuildSuffixTree("ATATCGTTTTATCGTT$")
    print "maxpattern:", ExtendSuffixTree.maxpattern
    #print suftree
    #PrintSuffix(suftree)


def mainLongPattern(text):
    BuildSuffixTree(text)
    print ExtendSuffixTree.maxpattern

if __name__ == "__main__":
    '''
    test()
    '''
    infile   = "/home/ajing/Downloads/dataset_94_8.txt"
    #infile   = "tmp2"
    text = open(infile).readlines()[0].strip() + "$"
    #stree = BuildSuffixTree(text)
    #PrintSuffix(stree)
    mainLongPattern(text)
