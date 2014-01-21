'''
Solve the Multiple Approximate Pattern Matching Problem.
    Input: A string Text, followed by a collection of strings Patterns, and an integer d.
    Output: All positions where one of the strings in Patterns appears as a substring of Text with at most d mismatches.
'''

import regex

def GetRE(pattern, d):
    reg = r'(?:' + pattern + "){s<=" + str(d) + "}"
    return reg

def MultipleApproxPatternMatch(text, patterns, d):
    all_matched_index = []
    for eachp in patterns:
        reg = GetRE(eachp, d)
        for m in regex.finditer(reg, text, overlapped = True):
            all_matched_index.append(m.start())
    all_matched_index.sort()
    print " ".join(map(str, all_matched_index))

def test():
    text = "ACATGCTACTTT"
    patterns = [ "ATT", "GCC", "GCTA", "TATT"]
    d = 1
    MultipleApproxPatternMatch(text, patterns, d)

if __name__ == "__main__":
    '''
    test()
    '''
    infile   = "tmp"
    infile   = "/home/ajing/Downloads/dataset_104_6.txt"
    content = [ x.strip() for x in open(infile).readlines()]
    text    = content[0]
    patterns= content[1].split()
    d = int(content[2])
    #print patterns, d
    MultipleApproxPatternMatch(text, patterns, d)
