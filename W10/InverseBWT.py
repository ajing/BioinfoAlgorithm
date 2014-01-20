'''
Inverse Burrows-Wheeler Transform Problem: Reconstruct a string from its Burrows-Wheeler transform.
    Input: A string Transform (with a single $ symbol).
    Output: The string Text such that BWT(Text) = Transform.
'''

def MapLastToFirst(bwt):
    firstcol = sorted(bwt)
    map_index = []
    for eachchar in bwt:
        index = firstcol.index(eachchar)
        map_index.append(index)
        firstcol[index] = "#"
    return map_index

def MapFirstToLast(bwt):
    maplast2first = MapLastToFirst(bwt)
    map_f2l = [ maplast2first.index(ind) for ind in range(len(maplast2first))]
    return map_f2l

def InverseBWT(bwt):
    firstcol = sorted(bwt)
    map_f2l = MapFirstToLast(bwt)
    startpoint = bwt.index("$")
    nextchar   = firstcol[startpoint]
    wholestr   = ""
    while nextchar != "$":
        wholestr += nextchar
        startpoint = map_f2l[startpoint]
        nextchar  = firstcol[startpoint]
    return wholestr + "$"

def test():
    text = "TTCCTAACG$A"
    InverseBWT(text)
    MapFirstToLast(text)

if __name__ == "__main__":
    #test()
    infile   = "/home/ajing/Downloads/dataset_99_10.txt"
    #infile   = "tmp"
    text = open(infile).readlines()[0].strip()
    print InverseBWT(text)
