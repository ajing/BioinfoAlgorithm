'''
    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection BestMotifs resulting from running RANDOMIZEDMOTIFSEARCH(Dna, k, t) 1000 times.
'''
from GreedyMotif import BuildProfilePseudo, _AMINO_INDEX_, ScoreMotifs
from ProfileMost import ProfileMost
from random import randint


def RandomizedMotif(dna, k):
    start = randint(0, len(dna) - k)
    return dna[start:start + k]

def RandomizedMotifList(dna_list, k):
    motif_list = []
    for i in range(len(dna_list)):
        motif_list.append(RandomizedMotif(dna_list[i], k))
    return motif_list

def MotifsBuildfromProfile(dna_list, k, profile):
    motifs = []
    for i in range(len(dna_list)):
        motif = ProfileMost(dna_list[i], k, _AMINO_INDEX_, profile)
        motifs.append(motif)
    return motifs

def RandomizedMotifSearch(dna_list, k, t):
    motifs = RandomizedMotifList(dna_list, k)
    best_score = 10000
    while True:
        profile = BuildProfilePseudo(motifs)
        motifs  = MotifsBuildfromProfile(dna_list, k, profile)
        score   = ScoreMotifs(motifs)
        if score < best_score:
            best_motifs = motifs[:]
            best_score  = score
        else:
            return best_motifs

def Runs1000Times(dna_list, k, t):
    best_score = 1000
    for i in range(1000):
        motifs = RandomizedMotifSearch(dna_list, k, t)
        if ScoreMotifs(motifs) < best_score:
            best_motifs = motifs
            best_score = ScoreMotifs(motifs)
    print best_score
    return best_motifs

if __name__ == "__main__":
    #dna = "ABC"
    #k = 2
    #print RandomizedMotif(dna, k)
    infile  = "/home/ajing/Downloads/dataset_41_4.txt"
    content = [line.strip() for line in open(infile).readlines()]
    k, t    = [int(x) for x in content[0].split()]
    seqs    = content[1:]
    content = [line.strip() for line in open(infile).readlines()]
    #print RandomizedMotifSearch(seqs, k, t)
    print "\n".join(Runs1000Times(seqs, k, t))
