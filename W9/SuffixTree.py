'''
Solve the Suffix Tree Construction Problem.
    Input: A string Text.
    Output: The edge labels of SuffixTree(Text). You may return these strings in any order.
'''

def IndexSame(string1, string2):
    min_s = min(len(string1), len(string2))
    for i in range(min_s):
        if string1[i] != string2[i]:
            return i

def MatchEdge( eachc, suffixtree, startnode):
    max_len = 0
    max_key = ""
    if startnode >= len(suffixtree):
        print "startnode is too large"
        return False
    for eachkey in suffixtree[startnode]:
        print eachkey
        index = IndexSame(eachkey, eachc)
        print index
        if  index > max_len:
            max_key = eachkey
            max_len = index
    if max_key:
        return max_key
    else:
        return False

def CurrentID():
    CurrentID.ID += 1
    return CurrentID.ID
CurrentID.ID = 1

def FindCommonPrefix(pattern, stree):
    print "pattern:", pattern
    startnode = 1
    startold  = 0
    matched_s = False
    matched_old = False
    while pattern:
        matched_old = matched_s
        matched_s = MatchEdge(pattern, stree, startnode)
        print "before:match:", matched_s, "pattern:", pattern
        if matched_s:
            index   = IndexSame(matched_s, pattern)
            pattern = pattern[index:]
            startold = startnode
            startnode, index = stree[startnode][matched_s]
        else:
            return pattern, startold, matched_old
        print "after:match:", matched_s, "pattern:", pattern

def ExtendSuffixTree(pattern_left, ematched, stree, matchnode, i):
    branch = stree[matchnode]
    print "ematched", ematched
    if ematched:
        # two new nodes with two new edges and one modified edge
        index = IndexSame(pattern_left, ematched)
        branch[ematched[index:]] = [ new_v, i ]
        new_v = CurrentID()
        stree.append({})
        new_w = CurrentID()
        print "new_w", new_w
        stree.append({"!":i})
        stree[new_v][ematched[:index]] = branch[ematched]
        stree[new_v][pattern_left[index:]] = [ new_w, i]
        del branch[ematched]
    else:
        new_v = CurrentID()
        stree.append({"!":i})
        branch[pattern_left] = [ new_v, i]
    print pattern_left, ematched, branch

def BuildSuffixTree(text):
    # suffix tree is like [0, {"CTG":(nextnode, startindex), "A"}, {}]
    patterns = [text[i:] + "$" for i in range(len(text))]
    suffixtree = [{},{}]
    for i in range(len(patterns)):
        eachp  = patterns[i]
        patternleft, nodematched, edgematched = FindCommonPrefix(eachp, suffixtree)
        print "nodematch:",nodematched
        ExtendSuffixTree( patternleft, edgematched, suffixtree, nodematched, i)
        print "suffixtree:", suffixtree

def test():
    BuildSuffixTree("ATAAATG")


if __name__ == "__main__":
    test()

