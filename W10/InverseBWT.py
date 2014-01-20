'''
Inverse Burrows-Wheeler Transform Problem: Reconstruct a string from its Burrows-Wheeler transform.
    Input: A string Transform (with a single $ symbol).
    Output: The string Text such that BWT(Text) = Transform.
'''

def InverseBWT(bwt):
    firstcol = sorted(bwt)
    map_index = []
    for eachchar in bwt:
        index = firstcol.index(eachchar)
        map_index.append(index)
        del firstcol[index]
    print map_index

def test():
    text = "TTCCTAACG$A"

if __name__ == "__main__":
    test()
