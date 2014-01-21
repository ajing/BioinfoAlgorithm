'''
Solve the Multiple Pattern Matching Problem.
    Input: A string Text followed by a collection of strings Patterns.
    Output: All starting positions in Text where a string from Patterns appears as a substring.
'''
from BWT import BWT
from BetterBWMatching import BetterBWMatching, CreateFirstOccur, CreateCountDict

def SuffixArray(text):
    return sorted( range(len(text)), key = lambda i: (text + text)[i:])

def SuffixArrayT(text, multiplier):
    index = sorted( range(len(text)), key = lambda i: (text + text)[i:])
    return [ (index.index(x), x) for x in index if not x % multiplier]

def MultiplePatternMatch(text, patterns):
    bwt = BWT(text + "$")
    firstcol = sorted(bwt)
    first_occur = CreateFirstOccur(firstcol)
    count_dict  = CreateCountDict(bwt)
    suffix_array= SuffixArray(text)
    all_matched_index = []
    for eachp in patterns:
        top, bottom = BetterBWMatching(first_occur, bwt, eachp, count_dict)
        if not top:
            continue
        matched_index = suffix_array[(top - 1): bottom]
        all_matched_index += matched_index
    all_matched_index.sort()
    print all_matched_index

def find_all(a_str, sub):
    start = 0
    res = []
    while True:
        start = a_str.find(sub, start)
        if start == -1:
          return res
        else:
          res.append(start)
        start += len(sub)
    return res

def FakeMultiMatch(text, patterns):
    all_matches = []
    for eachp in patterns:


def test():
    text = "AATCGGGTTCAATCGGGGT"
    patterns = [ "ATCG", "GGGT"]
    print SuffixArrayT(text, 1)
    MultiplePatternMatch(text, patterns)

if __name__ == "__main__":
    #test()
    infile   = "tmp"
    content = [ x.strip() for x in open(infile).readlines()]
    text    = content[0]
    patterns= content[1:]
    print patterns
    MultiplePatternMatch(text, patterns)
