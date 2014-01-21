'''
Construct a partial suffix array.
    Input: A string Text and a positive integer K.
    Output: SuffixArrayK(Text), in the form of a list of ordered pairs (i, SuffixArray(i)) for all nonempty entries in the partial suffix array.
'''

def SuffixArray(text, multiplier):
    index = sorted( range(len(text)), key = lambda i: (text + text)[i:])
    return [ (index.index(x), x) for x in index if not x % multiplier]

def PrintSuffixArray(su_array):
    for each in su_array:
        print ",".join(map(str, each))

def test():
    bwt = "PANAMABANANAS$"
    sarray = SuffixArray(bwt, 1)
    PrintSuffixArray(sarray)

if __name__ == "__main__":
    test()
    '''
    infile   = "/home/ajing/Downloads/dataset_102_3.txt"
    #infile   = "tmp"
    text, multi = [ x.strip() for x in open(infile).readlines()]
    multi    = int(multi)
    sarray   = SuffixArray(text, multi)
    PrintSuffixArray(sarray)
    '''
