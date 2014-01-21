'''
Solve the Multiple Approximate Pattern Matching Problem.
    Input: A string Text, followed by a collection of strings Patterns, and an integer d.
    Output: All positions where one of the strings in Patterns appears as a substring of Text with at most d mismatches.
'''

import regex
from multiprocessing import Pool
import math

def GetRE(pattern, d):
    reg = r'(?:' + pattern + "){s<=" + str(d) + "}"
    return reg

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def MultipleApproxPatternMatch(inputset):
    patterns, d = inputset
    all_matched_index = []
    for eachp in patterns:
        reg = GetRE(eachp, d)
        for m in regex.finditer(reg, text, overlapped = True):
            all_matched_index.append(m.start())
    return all_matched_index

def test():
    text = "ACATGCTACTTT"
    patterns = [ "ATT", "GCC", "GCTA", "TATT"]
    d = 1
    #MultipleApproxPatternMatch(text, patterns, d)
    Multiprocessor(text, patterns, d, 2)

def Multiprocessor(text, patterns, d, k):
    # k is the number of processors
    part_len      = math.ceil(len(patterns) / k)
    patterns_list = list(chunks(patterns, k))
    argumentlist  = []
    for eachp in patterns_list:
        argumentlist.append((eachp, d))
    MultipleApproxPatternMatch(argumentlist[0])
    pool = Pool(processes = k)
    result = pool.map_async(MultipleApproxPatternMatch, argumentlist)
    matched_list    = result.get()
    matched_flatten = [item for sublist in matched_list for item in sublist]
    matched_flatten.sort()
    print " ".join(map(str, matched_flatten))

if __name__ == "__main__":
    '''
    test()
    '''
    global text
    infile   = "tmp"
    infile   = "/home/ajing/Downloads/dataset_104_6.txt"
    content = [ x.strip() for x in open(infile).readlines()]
    text    = content[0]
    patterns= content[1].split()
    d = int(content[2])
    #print patterns, d
    #MultipleApproxPatternMatch(text, patterns, d)
    Multiprocessor(text, patterns, d, 5)
