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
    max_ind = 0
    max_key = False
    for eachkey in suffixtree[startnode]:
        index = IndexSame(eachkey, eachc)
        if  index > max_ind:
            max_key = eachkey
            max_ind = index
    return max_key

def CurrentID():
    CurrentID.ID += 1
    return CurrentID.ID

def FindCommonPrefix(pattern, stree):
    startnode = 1
    startold  = startnode
    matched_s = False
    matched_old = False
    pattern_old = pattern
    while pattern:
        matched_old = matched_s
        matched_s = MatchEdge(pattern, stree, startnode)
        if matched_s:
            index   = IndexSame(matched_s, pattern)
            pattern_old = pattern
            pattern = pattern[index:]
            startold = startnode
            startnode, index = stree[startnode][matched_s]
        else:
            #print "pattern_old:", pattern_old, startold, matched_old
            if matched_old in stree[startnode]:
                return pattern, startnode, matched_s
            else:
                return pattern_old, startold, matched_old

def ExtendSuffixTree(pattern_left, ematched, stree, matchnode, i):
    branch = stree[matchnode]
    if ematched:
        # two new nodes with two new edges and one modified edge
        index = IndexSame(pattern_left, ematched)
        new_v = CurrentID()
        stree.append({})
        new_w = CurrentID()
        stree.append({"!":i})
        #print "branch", branch
        branch[ematched[:index]] = [ new_v, i ]
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
    # suffix tree is like [0, {"CTG":(nextnode, startindex), "A"}, {}]
    patterns = [text[i:] for i in range(len(text))]
    suffixtree = [{},{}]
    for i in range(len(patterns)):
        eachp  = patterns[i]
        #print "eachp:", eachp
        patternleft, nodematched, edgematched = FindCommonPrefix(eachp, suffixtree)
        ExtendSuffixTree( patternleft, edgematched, suffixtree, nodematched, i)
        #print "suffixtree:", suffixtree
    return suffixtree

def test():
    suftree = BuildSuffixTree("ATAAA$")
    print suftree
    PrintSuffix(suftree)
    #print IndexSame("A", "AA")


if __name__ == "__main__":
    #test()
    infile   = "/home/ajing/Downloads/dataset_93_3.txt"
    text = open(infile).readlines()[0].strip()
    stree = BuildSuffixTree(text)
    PrintSuffix(stree)
