'''
    LeaderBoardCyclopeptideSequencing
    Input: Integer N and a collection of integers Spectrum.
'''
# rewrite function in numpy so quicker functions
from CyclopeptideSeq import *
'''
import numpy as np
def SubPeptideMass( peptide, length ):
    # peptide is a numpy array
    if len(peptide) == length:
        return [np.sum(peptide)]
    masslist = []
    pep_len  = len(peptide)
    for i in range(pep_len):
        mass = np.sum(np.roll(peptide, i)[:length])
        masslist.append(mass)
    return masslist

def AllPossibleSubMass( peptide ):
    pep_len = len(peptide)
    all_possible = [0]
    for i in range(1, pep_len + 1):
        all_possible += SubPeptideMass(peptide, i)
    return all_possible

def Cyclospectrum(aacid_mass_list):
    mass_sum = AllPossibleSubMass(aacid_mass_list)
    return sorted(mass_sum)
'''

def Mass(peptide):
    return sum(peptide)

def ParentMass(spectrum):
    return max(spectrum)

def Score(peptide, spectrum):
    score = 0
    spect_copy = list(spectrum)
    pep_spect  = Linearspectrum(peptide)
    for amino_acid in pep_spect:
        if amino_acid in spect_copy:
            score += 1
            spect_copy.remove(amino_acid)
    return score

def TopNIndexfromList(alist, topN):
    # top N from a sorted list including ties
    alist_len = len(alist)
    if topN > alist_len:
        return alist_len
    elementN = alist[topN-1]
    for each in range(topN - 1, alist_len):
        if alist[each] != elementN:
            break
    return each

def ReturnScoreList(peptidelist, spectrum):
    scorelist = []
    for each in peptidelist:
        scorelist.append(Score(each, spectrum))
    return scorelist

def Cut(leaderboard, spectrum, topN):
    # returns the top N highest-scoring peptides in Leaderboard (including ties) with respect to Spectrum.
    scorelist          = ReturnScoreList(leaderboard, spectrum)
    zip_sorted         = sorted(zip(scorelist, leaderboard), reverse = True)
    scorelist_sort     = []
    leaderboard_sort   = []
    for (score, peptide) in zip_sorted:
        scorelist_sort.append(score)
        leaderboard_sort.append(peptide)
    last_element_index = TopNIndexfromList(scorelist_sort, topN)
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
    # Test for Cyclospectrum
    peptide = "113-71-71-71-71-129".split("-")
    peptide = map(int, peptide)
    print Cyclospectrum(peptide)
    # reference 0 113 71 71 71 71 129 184 142 142 142 200 242 255 213 271 313 313 326 284 342 384 384 384 397 413 455 455 455 455 526
    # Test for Score()
    print Score([0,1,1],[0,1,1,1,2])
    #assert(Score([0,1,1],[0,1,1,1,2]) == 3)
    '''
    spectrum = "0 71 113 129 147 200 218 260 313 331 347 389 460".split()
    spectrum = map(int, spectrum)
    N = 10
    leaderpeptide = LeaderCyclopeptideSequencing(spectrum, N)
    print "-".join(map(str, leaderpeptide))
    '''

if __name__ == "__main__":
    '''
    SampleTest()
    '''
    infile = "/home/ajing/Downloads/dataset_24_4.txt"
    #infile = "input.txt"
    N, spectrum = [ x.strip() for x in open(infile).readlines()]
    N        = 30
    spectrum = map(int, spectrum.split())
    leaderpeptide = LeaderCyclopeptideSequencing(spectrum, N)
    print "-".join(map(str, leaderpeptide))
    print len(leaderpeptide)
