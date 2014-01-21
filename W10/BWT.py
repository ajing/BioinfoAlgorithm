'''
Burrows-Wheeler Transform Construction Problem: Construct the Burrows-Wheeler transform of a string.
   Input: A string Text.
   Output: BWT(Text).
'''

def BWT(text):
    index = sorted(range(len(text)), key = lambda i: (text + text)[(i + 1) :])
    sortlist = [text[i] for i in index]
    return sortlist

def test():
    text = "GCGTGCCTGGTCA$"
    print "".join(BWT(text))

if __name__ == "__main__":
    #test()
    infile   = "/home/ajing/Downloads/dataset_97_4.txt"
    #infile   = "tmp"
    text = open(infile).readlines()[0].strip()
    print "".join(BWT(text))
