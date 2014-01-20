'''
Implement BWMATCHING.
    Input: A string BWT(Text), followed by a collection of Patterns.
    Output: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.
'''

from InverseBWT import MapLastToFirst

def BWMatching(firstcolumn, lastcolumn, pattern, last2first):
    top = 0
    bottom = len(lastcolumn) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            last_short = lastcolumn[top : (bottom + 1)]
            print symbol, pattern, last_short
            if symbol in last_short:
                topIndex  = last_short.index(symbol) + top
                lastIndex = len(last_short) - last_short[::-1].index(symbol) + top + 1
                print topIndex, lastIndex
                top    = last2first[topIndex]
                bottom = last2first[lastIndex]
            else:
                return 0
        else:
            return bottom - top + 1

def main(bwt, patterns):
    firstcol = sorted(bwt)
    last2first = MapLastToFirst(bwt)
    num_matchs = []
    for eachp in patterns:
        num_matchs.append(BWMatching(firstcol, bwt, eachp, last2first))

def test():
    bwt = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
    patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]
    main(bwt, patterns)

if __name__ == "__main__":
    test()
