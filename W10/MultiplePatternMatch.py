'''
Solve the Multiple Pattern Matching Problem.
    Input: A string Text followed by a collection of strings Patterns.
    Output: All starting positions in Text where a string from Patterns appears as a substring.
'''
from BWT import BWT
from BetterBWMatching import BetterBWMatching, CreateFirstOccur, CreateCountDict
from InverseBWT import MapLastToFirst

def SuffixArray(text):
    return sorted( range(len(text)), key = lambda i: (text + text)[i:])

def MultiplePatternMatch(text, patterns):
    bwt = BWT(text + "$")
    firstcol = sorted(bwt)
    first_occur = CreateFirstOccur(firstcol)
    count_dict  = CreateCountDict(bwt)
    suffix_array= SuffixArray(text + "$")
    all_matched_index = []
    for eachp in patterns:
        top, bottom = BetterBWMatching(first_occur, bwt, eachp, count_dict)
        if not top:
            continue
        matched_index = suffix_array[top : (bottom + 1)]
        all_matched_index += matched_index
    all_matched_index.sort()
    print " ".join(map(str, all_matched_index))

def test():
    text = "AATCGGGTTCAATCGGGGT"
    patterns = [ "ATCG", "GGGT"]
    MultiplePatternMatch(text, patterns)

if __name__ == "__main__":
    '''
    test()
    '''
    infile   = "tmp"
    infile   = "/home/ajing/Downloads/dataset_103_4.txt"
    content = [ x.strip() for x in open(infile).readlines()]
    text    = content[0]
    patterns= content[1:]
    MultiplePatternMatch(text, patterns)
