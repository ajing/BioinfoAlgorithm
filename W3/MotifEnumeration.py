'''
   Input: Integers k and d, followed by a collection of strings Dna.
   Output: All (k, d)-motifs in Dna.
'''
import sys
sys.path.append("../W1")
from FrequentWord import FuzzyMatching, PatternGenerator

def EachKMer(Dna, k):
    dna_len = len(Dna)
    for i in range(dna_len - k + 1):
        yield Dna[i:i+k]

def KmerMutation(kmer, d):
    pass


def Appear(kmer, each_Dna, d):
    dna_len = len(each_Dna)
    pat_len = len(kmer)
    for i in range(dna_len - pat_len + 1):
        if FuzzyMatching(each_Dna[i:i + pat_len], kmer, d):
            return True
    return False

def AppearInAll(kmer, Dna_list, d):
    for each_Dna in Dna_list:
        if not Appear(kmer, each_Dna, d):
            return False
    return True

def MotifEnumerate(DnaList, k, d):
    #print DnaList
    kmer_list = []
    for eachKmer in PatternGenerator(k):
        if AppearInAll(eachKmer, DnaList, d) and not eachKmer in kmer_list:
            kmer_list.append(eachKmer)
    print len(kmer_list)
    print " ".join(kmer_list)

if __name__ == "__main__":
    #DnaList = "AAATTGACGCAT\nGACGACCACGTT\nCGTCAGCGCCTG\nGCTGAGCACCGG\nAGTACGGGACAG"
    #DnaList = "ATTTGGC\nTGCCTTA\nCGGTATC\nGAAAATT"
    infile  = "/home/ajing/Downloads/dataset_36_7.txt"
    content = [line.strip() for line in open(infile).readlines()]
    seqs    = content[1:]
    k, d = [ int(x) for x in content[0].split() ]
    print k, d, seqs
    MotifEnumerate( seqs, k, d)
