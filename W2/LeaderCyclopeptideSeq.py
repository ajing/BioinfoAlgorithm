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
    scorelist          = ReturnScoreList(leaderboard_sort, spectrum)
    last_element_index = TopNIndexfromList(scorelist, topN)
    return leaderboard_sort[:(last_element_index + 1)]

def LeaderCyclopeptideSequencing(spectrum_list, TopN):
    # clean spectrum_list
    LeaderBoard   = [0]
    LeaderPeptide = []
    while LeaderBoard:
    #for i in range(2):
        LeaderBoard = Expand(LeaderBoard)
        LeaderBoard_new = []
        for peptide in LeaderBoard:
            if Mass(peptide) == ParentMass(spectrum_list):
                if Score(peptide, spectrum_list) > Score(LeaderPeptide, spectrum_list):
                    LeaderPeptide = peptide
            if Mass(peptide) <= ParentMass(spectrum_list):
                LeaderBoard_new.append(peptide)
        #print "before cut", ReturnScoreList(LeaderBoard_new, spectrum_list)
        LeaderBoard_new = Cut(LeaderBoard_new, spectrum_list, TopN)
        #print "after cut", ReturnScoreList(LeaderBoard_new, spectrum_list)
        #print "3:", ReturnScoreList(LeaderBoard_new, spectrum_list).count(3)
        #print len(LeaderBoard_new)
        LeaderBoard = LeaderBoard_new
    return LeaderPeptide

if __name__ == "__main__":
    infile = "/home/ajing/Downloads/dataset_24_4.txt"
    for x in open(infile).readlines():
        print x
    N, spectrum = [ x.strip() for x in open(infile).readlines()]
    N        = int(N)
    #N        = 10
    #spectrum = "0 71 113 129 147 200 218 260 313 331 347 389 460"
    spectrum = map(int, spectrum.split())
    peptide = [156, 71, 113, 114, 131, 156, 113, 101, 129, 128, 128, 114, 128, 103, 97, 131, 131, 113, 131, 113, 128, 115, 128, 113]
    leaderpeptide = LeaderCyclopeptideSequencing(spectrum, N)
    print leaderpeptide
    print len(leaderpeptide)
