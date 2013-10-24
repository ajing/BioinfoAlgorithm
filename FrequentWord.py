"""
    Find k-mer for the file
"""

import os
import itertools
from ReverseComplement import *

def KmerForLine(line, n):
    line_len = len(line)
    kmerdict = dict()
    for i in range(line_len - n + 1):
        kmer = line[i:i+n]
        try:
            kmerdict[kmer] += 1
        except:
            kmerdict[kmer] = 1
    maximun = max(kmerdict.values())
    bestkmerlist = [i for i,x in kmerdict.items() if x == maximun]
    return kmerdict

def PatternGenerator( pattern_len ):
    dna = ["A","T","C","G"]
    for combine in itertools.combinations_with_replacement( dna, pattern_len ):
        for order in itertools.permutations( combine, pattern_len):
            yield "".join(order)

def KmerFuzzy(Seq, k, d):
    Seq_len = len(Seq)
    kmerdict = dict()
    for eachPattern in PatternGenerator(k):
        if eachPattern in kmerdict:
            continue
        kmerdict[eachPattern] = len(PatternMatching(Seq, eachPattern, d))
    print Seq
    maximun = max(kmerdict.values())
    bestkmerlist = [i for i,x in kmerdict.items() if x == maximun]
    print " ".join(bestkmerlist)


def KmerDictUpdate(ori_kmer_dict, new_kmer_dict):
    for each in new_kmer_dict:
        try:
            ori_kmer_dict[each] = max( [ori_kmer_dict[each], new_kmer_dict[each]] )
        except:
            ori_kmer_dict[each] = new_kmer_dict[each]
    return ori_kmer_dict

def ClumpFind(Seq, n, L, t):
    seq_len = len(Seq)
    clump_dict = dict()
    for i in range(seq_len - L):
        sub_seq = Seq[i:i + L]
        kmerdict = KmerForLine(sub_seq, n)
        clump_dict = KmerDictUpdate(clump_dict, kmerdict)
    clump_list = []
    for each_sub in clump_dict:
        if clump_dict[each_sub] >= t:
            clump_list.append(each_sub)
    print " ".join(clump_list)

def FileReader(infile):
    firstline = 1
    for each in open(infile):
        line = each.strip()
        if firstline:
            fline = line
            firstline = 0
        else:
            sline = line
    return (fline, sline)

def main():
    #infile = "./Data/stepic_dataset.txt"
    infile = "/home/jing/Downloads/stepic_dataset.txt"
    firstline = 1
    for each in open(infile):
        line = each.strip()
        if firstline:
            seq = line
            firstline = 0
        else:
            kmer = int(line)
    KmerForLine(seq, kmer)

def main2():
    '''
    #test case
    seq = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    k = 5
    L = 50
    t = 4
    ClumpFind(seq, k, L, t)
    '''
    infile = "/home/jing/Downloads/stepic_dataset.txt"
    seq, secondline = FileReader(infile)
    k, L, t  = map(int, secondline.split(" "))
    print k,L,t
    ClumpFind(seq, k, L, t)

def mainKF():
    '''
    # test case
    # 1 test pattern generator
    seq = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d = 1
    KmerFuzzy(seq, k, d)
    '''
    infile = "/home/jing/Downloads/dataset_8_4.txt.txt"
    content = open(infile).readlines()
    seq, k, d = content[0].split()
    k = int(k)
    d.strip()
    d = int(d)
    KmerFuzzy(seq, k, d)

def mainKFReverse():
    '''
    # test case
    # 1 test pattern generator
    seq = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d = 1
    KmerFuzzy(seq, k, d)
    '''
    infile = "/home/jing/Downloads/dataset_8_5.txt.txt"
    content = open(infile).readlines()
    seq = content[0].strip()
    k, d = content[1].strip().split()
    k = int(k)
    d = int(d)
    print seq, k, d
    KmerFuzzy(seq, k, d)

if __name__ == "__main__":
    #main()
    #main2()
    #mainKF()
    mainKFReverse()
