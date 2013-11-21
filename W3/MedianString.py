'''
   Input: An integer k, followed by a collection of strings Dna.
   Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern.
'''

import sys
sys.path.append("../W1")
from FrequentWord import PatternGenerator
from MotifEnumeration import AppearInAll

def ScorePattern(kmer, motif):
    score = 0
    for each in zip(kmer, motif):
        if each[0] != each[1]:
            score += 1
    return score

def ScoreDna(kmer, Dna):
    dna_len = len(Dna)
    pat_len = len(kmer)
    score   = []
    for i in range(dna_len - pat_len + 1):
        score.append(ScorePattern(kmer, Dna[i:i + pat_len]))
    return min(score)

def Score(kmer, Dna_list):
    total = 0
    for each_dna in Dna_list:
        total += ScoreDna(kmer, each_dna)
    return total

def MedianString(Dna_list, k):
    best_pattern = "A" * k
    patterndict  = dict()
    score        = dict()
    for eachpattern in PatternGenerator(k):
        if not eachpattern in score:
            score[eachpattern] = Score(eachpattern, Dna_list)
    minval = min(score, key = score.get)
    print score
    print minval, score[minval]

if __name__ == "__main__":
    #print Score("AAB", ["ABC", "AAB"])
    #MedianString(["AAAB", "AAAC"], 3)
    infile  = "/home/ajing/Downloads/dataset_38_7.txt"
    content = [line.strip() for line in open(infile).readlines()]
    seqs    = content[1:]
    k       = int(content[0])
    MedianString(seqs, k)
