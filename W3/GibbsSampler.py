'''
     Input: Integers k, t, and N, followed by a collection of strings Dna.
     Output: The strings BestMotifs resulting from running GIBBSSAMPLER(Dna, k, t, N) with 20 random starts.
'''
from RandomMotif import *
from RandomMotif import _AMINO_INDEX_
from ProfileMost import Prob

import random
import bisect
import collections

def ProfileRandom(dna, k, amino_index, profile):
    def cdf(weights):
        total=sum(weights)
        result=[]
        cumsum=0
        for w in weights:
            cumsum+=w
            result.append(cumsum/total)
        return result

    def choice(population,weights):
        assert len(population) == len(weights)
        cdf_vals=cdf(weights)
        x=random.random()
        idx=bisect.bisect(cdf_vals,x)
        return population[idx]

    dna_len   = len(dna)
    motifs    = []
    weights   = []
    for i in range(dna_len - k + 1):
        motif = dna[i:i + k]
        motifs.append(motif)
        weights.append(Prob(motif, amino_index, profile))

    return choice(motifs, weights)


def GibbsSampler(dna_list, k, t, N):
    # t: number of sequence
    motifs = RandomizedMotifList(dna_list, k)
    best_score = 10000
    for i in range(N):
        j = randint(0,t - 1)
        new_motifs = motifs[:j] + motifs[(j + 1):]
        profile = BuildProfilePseudo(new_motifs)
        #print profile
        motifs[j] = ProfileRandom(dna_list[j], k, _AMINO_INDEX_, profile)
        score     = ScoreMotifs(motifs)
        if score < best_score:
            best_motifs = motifs[:]
            best_score  = score
    return best_motifs, best_score

def Runs1000Times(dna_list, k, t, N):
    best_score = 10000
    for i in range(40):
        motifs, score = GibbsSampler(dna_list, k, t, N)
        if score < best_score:
            best_motifs = motifs
            best_score  =  score
    print best_score
    return best_motifs

def test():
    seq = "TACGCA"
    profile = [[0, 0.5, 0, 0.5],[1, 0, 0, 0]]
    print ProfileRandom(seq, 2, _AMINO_INDEX_, profile)

if __name__ == "__main__":
    '''
    test()
    '''
    infile  = "/home/ajing/Downloads/dataset_43_4.txt"
    content = [line.strip() for line in open(infile).readlines()]
    k, t, N   = [int(x) for x in content[0].split()]
    seqs    = content[1:]
    print k, t, N, seqs
    motifs  = Runs1000Times(seqs, k, t, N)
    print "\n".join(motifs)
    print ScoreMotifs(motifs)
    motifs  = ['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']
    print ScoreMotifs(motifs)
