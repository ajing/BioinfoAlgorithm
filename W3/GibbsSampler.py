'''
     Input: Integers k, t, and N, followed by a collection of strings Dna.
     Output: The strings BestMotifs resulting from running GIBBSSAMPLER(Dna, k, t, N) with 20 random starts.
'''
from RandomMotif import *
from RandomMotif import _AMINO_INDEX_

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

    dna_len   = len(seq)
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
    best_score = 1000
    N = 100000
    for i in range(N):
        i = randint(0,t - 1)
        new_motifs = motifs[:i] + motifs[(i + 1):]
        profile = BuildProfilePseudo(new_motifs)
        #print profile
        motifs[i] = ProfileMost(dna_list[i], k, _AMINO_INDEX_, profile)
        score     = ScoreMotifs(motifs)
        if score < best_score:
            best_motifs = motifs
            best_score  = score
    return best_motifs

def Runs1000Times(dna_list, k, t, N):
    best_score = 1000
    for i in range(2000):
        motifs = GibbsSampler(dna_list, k, t, N)
        if ScoreMotifs(motifs) < best_score:
            best_motifs = motifs
            best_score = ScoreMotifs(motifs)
    print best_score
    return best_motifs


if __name__ == "__main__":
    infile  = "/home/ajing/Downloads/dataset_40_9.txt"
    content = [line.strip() for line in open(infile).readlines()]
    k, t, N    = [int(x) for x in content[0].split()]
    seqs    = content[1:]
    print k, t, N, seqs
    #print "\n".join(Runs1000Times(seqs, k, t, N))
