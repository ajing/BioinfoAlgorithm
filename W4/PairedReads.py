'''
    Solve the String Reconstruction from Read-Pairs Problem.
    Input: An integer d followed by a collection of paired k-mers PairedReads.
    Output: A string Text with (k, d)-mer composition equal to PairedReads.
'''

from EulerianPath import EulerianPath, JoinPathtoString
from DeBruijn import SimpList


def DeBruijnPaired(pairs):
    adj_list = []
    for eachpair in pairs:
        first_pair  = tuple([x[:-1] for x in eachpair])
        second_pair = tuple([x[1:] for x in eachpair])
        adj_list.append([first_pair, second_pair])
    collapse_dict = SimpList(adj_list)
    return collapse_dict

def PairfileParser(infile):
    flag = 1
    pairs = []
    for line in open(infile):
        content = line.strip()
        if flag:
            d = int(content)
            flag = 0
            continue
        start, end = content.split("|")
        pairs.append(tuple([start, end]))
    return d, pairs

def Path2Seq(path, d):
    startseq = path[0][0][:-1]
    endseq   = path[0][1][:-1]
    k = len(path[0][0])
    for each in path:
        startseq += each[0][-1]
        endseq += each[1][-1]
    return startseq[:(k + d + 1)] + endseq

def PairedReads(d, pairs):
    graph = DeBruijnPaired(pairs)
    path  = EulerianPath(graph)
    seq   = Path2Seq(path, d)
    print seq

if __name__ == "__main__":
    infile  = "/home/ajing/Downloads/dataset_58_14.txt"
    d, pairs = PairfileParser(infile)
    PairedReads(d, pairs)
