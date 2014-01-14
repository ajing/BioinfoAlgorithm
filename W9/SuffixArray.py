'''
Constructing Suffix Array Problem: Construct the suffix array of a string.
     Input: A string Text.
     Output: SuffixArray(Text).
'''

def SuffixArray(text):
    # text is ended with $
    if text[-1] != "$":
        text += "$"
    sarray  = sorted(range(len(text)), key = lambda i: text[i:])
    print ", ".join([str(x) for x in sarray])

def test():
    SuffixArray("ABC")
    SuffixArray("AACGATAGCGGTAGA")

if __name__ == "__main__":
    '''
    test()
    '''
    infile   = "/home/ajing/Downloads/dataset_95_6.txt"
    infile   = "tmp2"
    text = open(infile).readlines()[0].strip()
    SuffixArray(text)
