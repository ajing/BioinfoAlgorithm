"""
    Find k-mer for the file
"""

import os

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
    bestkmerlist = []
    for each in kmerdict:
        if kmerdict[each] == maximun:
            bestkmerlist.append(each)
    #print "\t".join(bestkmerlist) 
    return kmerdict

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

if __name__ == "__main__":
    #main()
    main2()
