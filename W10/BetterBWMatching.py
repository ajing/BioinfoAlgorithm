'''
Implement BETTERBWMATCHING.
    Input: A string BWT(Text) followed by a collection of strings Patterns.
    Output: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.
'''

alphabet = ["A", "T", "C", "G", "$"]

def CreateCountDict(lastcolumn):
    count_dict = dict()
    for eacha in alphabet:
        count_dict[eacha] = [0] * (len(lastcolumn) + 1)
    for i in range(len(lastcolumn)):
        a_acid = lastcolumn[i]
        for eacha in alphabet:
            if eacha == a_acid:
                count_dict[eacha][i + 1] = count_dict[eacha][i] + 1
            else:
                count_dict[eacha][i + 1] = count_dict[eacha][i]
    return count_dict

def CreateFirstOccur(firstcolumn):
    firstoccur = dict()
    for each in alphabet:
        firstoccur[each] = firstcolumn.index(each)
    return firstoccur

def BetterBWMatching(firstoccur, lastcolumn, pattern, countdict):
    top = 0
    bottom = len(lastcolumn) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            last_short = lastcolumn[top : (bottom + 1)]
            if symbol in last_short:
                top    = firstoccur[symbol] + countdict[symbol][top]
                bottom = firstoccur[symbol] + countdict[symbol][bottom + 1] - 1
            else:
                return False, False
        else:
            return top, bottom

def main(bwt, patterns):
    firstcol = sorted(bwt)
    first_occur = CreateFirstOccur(firstcol)
    count_dict  = CreateCountDict(bwt)
    num_matchs = []
    for eachp in patterns:
        top, bottom = BetterBWMatching(first_occur, bwt, eachp, count_dict)
        num_matchs.append(bottom - top + 1)
    print " ".join(map(str, num_matchs))

def test():
    #global alphabet
    #lastcolumn = "smnpbnnaaaaa$a"
    #alphabet   = set(list(lastcolumn))
    #print CreateCountDict(lastcolumn)
    #print CreateFirstOccur(sorted(lastcolumn))
    text = "GGCGCCGC$TAGTCACACACGCCGTA"
    patterns = [ "ACC", "CCG", "CAG"]
    main(text, patterns)

if __name__ == "__main__":
    '''
    test()
    '''
    infile   = "/home/ajing/Downloads/dataset_101_6.txt"
    #infile   = "tmp"
    text, patterns = [ x.strip() for x in open(infile).readlines()]
    patterns = patterns.split()
    #print text, patterns
    main(text, patterns)
