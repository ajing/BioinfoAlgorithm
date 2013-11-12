'''
    Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
    Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).
'''

from SpecConvolution import Convolution
from LeaderCyclopeptideSeq import *

def UniqueList(seq):
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

def ConvolFilter(convollist):
    new_convol  = []
    for each in convollist:
        if each >= 57 and each <= 200:
            new_convol.append(each)
    return new_convol

def ConvolutionSequencing(spectrum_list, topM, topN):
    convol_list = Convolution(spectrum_list)
    convol_set  = UniqueList(convol_list)
    convol_set  = ConvolFilter(convol_set)
    mass_count  = []
    for each in convol_set:
        mass_count.append(convol_list.count(each))
    print mass_count
    top_m_index = TopNIndexfromList(mass_count, topM)
    mass_list   = convol_set[:top_m_index]
    print "masslist:", mass_list
    print "masslist length:", len(mass_list)
    peptidemass = LeaderCyclopeptideSequencing(spectrum_list, topN, sorted(mass_list))
    print "-".join(map(str, peptidemass))


def Test():
    listint = "57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493".split()
    listint = map(int, listint)
    ConvolutionSequencing(listint, 20, 60)

if __name__ == "__main__":
    infile = "input.txt"
    M, N, listint = [x.strip() for x in open(infile).readlines()]
    print listint, M, N
    listint = map(int, listint.split())
    M = int(M)
    N = int(N)
    print listint, M, N
    ConvolutionSequencing(listint, M, N)
