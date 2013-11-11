'''
    LeaderBoardCyclopeptideSequencing
    Input: Integer N and a collection of integers Spectrum.
'''
from CyclopeptideSeq import *

def Mass(peptide):
    return sum(peptide)

def ParentMass(spectrum):
    return max(spectrum)

def Score(peptide, spectrum):
    score = 0
    spect_copy = list(spectrum)
    for amino_acid in Cyclospectrum(peptide):
        if amino_acid in spect_copy:
            score += 1
            spect_copy.remove(amino_acid)
    return score

def TopNIndexfromList(alist, topN):
    # top N from a sorted list including ties
    if topN > len(alist):
        return len(alist)
    elementN = alist[topN-1]
    alist_rev = alist[::-1]
    lastelementN = len(alist) - alist_rev.index(elementN)
    return lastelementN

def ReturnScoreList(peptidelist, spectrum):
    scorelist = []
    for each in peptidelist:
        scorelist.append(Score(each, spectrum))
    return scorelist

def Cut(leaderboard, spectrum, topN):
    # returns the top N highest-scoring peptides in Leaderboard (including ties) with respect to Spectrum.
    leaderboard_sort = sorted(leaderboard, key = lambda k: Score(k, spectrum), reverse = True)
    scorelist          = map( Score, leaderboard)
    last_element_index = TopNIndexfromList(sorted(scorelist), topN)
    return leaderboard_sort[:(last_element_index + 1)]

def LeaderCyclopeptideSequencing(spectrum_list, TopN):
    # clean spectrum_list
    spectrum_list = sorted(spectrum_list)
    LeaderBoard   = [0]
    LeaderPeptide = []
    LeaderScore   = 0
    Parent_Mass   = ParentMass(spectrum_list)
    while LeaderBoard:
        LeaderBoard = Expand(LeaderBoard)
        LeaderBoard_new = []
        for peptide in LeaderBoard:
            if Mass(peptide) == Parent_Mass:
                if Score(peptide, spectrum_list) > LeaderScore:
                    LeaderPeptide = peptide
                    LeaderScore   = Score(LeaderPeptide, spectrum_list)
            if Mass(peptide) <= Parent_Mass:
                LeaderBoard_new.append(peptide)
        LeaderBoard_new = Cut(LeaderBoard_new, spectrum_list, TopN)
        LeaderBoard = LeaderBoard_new
    return LeaderPeptide

def SampleTest():
    # Test for Score()
    print Score([0,1,1],[0,1,1,1,2])
    #assert(Score([0,1,1],[0,1,1,1,2]) == 3)
    spectrum = "0 71 113 129 147 200 218 260 313 331 347 389 460".split()
    spectrum = map(int, spectrum)
    N = 10
    leaderpeptide = LeaderCyclopeptideSequencing(spectrum, N)
    print "-".join(map(str, leaderpeptide))

if __name__ == "__main__":
    '''
    SampleTest()
    '''
    infile = "/home/ajing/Downloads/dataset_24_4.txt"
    N, spectrum = [ x.strip() for x in open(infile).readlines()]
    N        = int(N)
    spectrum = map(int, spectrum.split())
    leaderpeptide = LeaderCyclopeptideSequencing(spectrum, N)
    print "-".join(map(str, leaderpeptide))
    print len(leaderpeptide)
