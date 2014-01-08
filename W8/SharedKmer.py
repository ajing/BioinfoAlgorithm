'''
 Given two strings, find all their shared k-mers.
    Input: An integer k and two strings.
    Output: All k-mers shared by these strings, in the form of ordered pairs (x, y).
'''
from string import maketrans
from collections import defaultdict
import itertools

def ReverseComplement(seq):
    ori = "ATCG"
    trans = "TAGC"
    trantab = maketrans(ori, trans)
    new_seq = seq.translate(trantab)
    return new_seq[::-1]

def ParseSeq(seq, k):
    seqdict = defaultdict(list)
    for i in range(len(seq) - k + 1):
        shortseq = seq[i:(i + k)]
        if not i in seqdict[shortseq]:
            seqdict[shortseq].append(i)
        shortreverse = ReverseComplement(shortseq)
        if not i in seqdict[shortreverse]:
            seqdict[shortreverse].append(i)
    return seqdict

def SharedKmer(seq1, seq2, k):
    # hash seq2 as it will be shorter
    seq2dict = ParseSeq(seq2, k)
    sharedlist = []
    for i in range(len(seq1) - k + 1):
        shortseq1 = seq1[i:(i + k)]
        if shortseq1 in seq2dict:
            product = list(itertools.product([i], seq2dict[shortseq1]))
            sharedlist += product
    print "\n".join(map(str, sharedlist))

if __name__ == "__main__":
    k = 3
    seq1 = "AAACTCATC"
    seq2 = "TTTCAAATC"
    infile  = "tmp"
    infile  = "/home/ajing/Downloads/dataset_90_2.txt"
    k, seq1, seq2 = [x.strip() for x in open(infile).readlines()]
    k = int(k)
    SharedKmer(seq1, seq2, k)
