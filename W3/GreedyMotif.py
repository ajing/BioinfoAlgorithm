'''
    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection of strings BestMotifs resulting from applying GREEDYMOTIFSEARCH(Dna,k,t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
'''

from MedianString import Score
from ProfileMost import ProfileMost, Prob
from itertools import groupby as g

_AMINO_INDEX_ = ["A", "C", "G", "T"]

def BuildProfile(motif_list):
    motif_len = len(motif_list[0])
    profile   = []
    for i in range(motif_len):
        ith        = [ x[i] for x in motif_list ]
        count_list = []
        for each in _AMINO_INDEX_:
            num_amino = ith.count(each)
            count_list.append(num_amino)
        count_prob = [ float(x)/sum(count_list) for x in count_list ]
        profile.append(count_prob)
    return profile

def BuildProfilePseudo(motif_list):
    motif_len = len(motif_list[0])
    profile   = []
    for i in range(motif_len):
        ith        = [ x[i] for x in motif_list ]
        count_list = []
        for each in _AMINO_INDEX_:
            num_amino = ith.count(each) + 1
            count_list.append(num_amino)
        count_prob = [ float(x)/sum(count_list) for x in count_list ]
        profile.append(count_prob)
    return profile

def MostCommon(L):
      return max(g(sorted(L)), key=lambda(x, v):(len(list(v)),-L.index(x)))[0]

def ScoreMotifs(motif_list):
    motif_len = len(motif_list[0])
    score_total = 0
    for i in range(motif_len):
        ith        = [ x[i] for x in motif_list ]
        mostcommon = MostCommon(ith)
        score      = len([ x for x in ith if x != mostcommon ])
        score_total += score
    return score_total

def GreedyMotifSearch(Dna_list, k, t):
    best_motif = [ x[:k] for x in Dna_list ]
    Dna_len    = len(Dna_list[0])
    Dna_num    = len(Dna_list)
    for i in range(Dna_len - k + 1):
        motif_list = []
        motif_list.append( Dna_list[0][i:i + k] )
        for j in range(1, Dna_num):
            profile = BuildProfile(motif_list)
            motif = ProfileMost(Dna_list[j], k, _AMINO_INDEX_, profile)
            motif_list.append(motif)
        if ScoreMotifs(motif_list) < ScoreMotifs(best_motif):
            best_motif = motif_list
    return best_motif

def GreedyMotifSearchPseudo(Dna_list, k, t):
    best_motif = [ x[:k] for x in Dna_list ]
    Dna_len    = len(Dna_list[0])
    Dna_num    = len(Dna_list)
    for i in range(Dna_len - k + 1):
        motif_list = []
        motif_list.append( Dna_list[0][i:i + k] )
        for j in range(1, Dna_num):
            profile = BuildProfilePseudo(motif_list)
            motif = ProfileMost(Dna_list[j], k, _AMINO_INDEX_, profile)
            motif_list.append(motif)
        if ScoreMotifs(motif_list) < ScoreMotifs(best_motif):
            best_motif = motif_list
    return best_motif

if __name__ == "__main__":
    #motifs = ["CAG", "CAG", "ATC"]
    #print BuildProfilePseudo(motifs)
    #print ScoreMotifs(motifs)
    infile  = "/home/ajing/Downloads/dataset_40_9.txt"
    content = [line.strip() for line in open(infile).readlines()]
    k, t    = [int(x) for x in content[0].split()]
    seqs    = content[1:]
    #print k,t, seqs
    #print "\n".join(GreedyMotifSearch(seqs, k, t))
    print "\n".join(GreedyMotifSearchPseudo(seqs, k, t))
