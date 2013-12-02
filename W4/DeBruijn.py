'''
     Input: An integer k and a string Text.
     Output: DeBruijnk(Text).
'''
from StringComp import StringComp
from collections import defaultdict

def SimpList(adjlist):
    collapse_dict = defaultdict(list)
    for start, end in adjlist:
        collapse_dict[start].append(end)
    return collapse_dict

def DeBruijnk(seq, N):
    # return adjacency list of the de Bruijn graph DeBruijn(Patterns) from sequence.
    motif_list    = StringComp(seq, N - 1)
    adj_list      = zip(motif_list[:-1], motif_list[1:])
    collapse_dict = SimpList(adj_list)
    return collapse_dict

def PrintDict(col_dict):
    col_sets = col_dict.items()
    col_list = [list(x) for x in col_sets]
    col_list = sorted(col_list, key = lambda k: k[0])
    for start, end in col_list:
        end = list(set(end))
        print " -> ".join([start, ",".join(sorted(end))])

def DeBruijn_main():
    #PrintDict(DeBruijnk("AAGATTCTCTAC", 4))
    infile  = "/home/ajing/Downloads/dataset_53_6.txt"
    content = [line.strip() for line in open(infile).readlines()]
    N       = int(content[0])
    Seq     = content[1]
    PrintDict(DeBruijnk(Seq, N))

def DeBruijnKmer(seqs):
    # return adjacency list of the de Bruijn graph DeBruijn(Patterns) from kmers.
    adj_list = []
    for eachseq in seqs:
        adj_list.append([eachseq[:-1], eachseq[1:]])
    collapse_dict = SimpList(adj_list)
    return collapse_dict

if __name__ == "__main__":
    #DeBruijn_main()
    infile  = "/home/ajing/Downloads/dataset_54_7.txt"
    content = [line.strip() for line in open(infile).readlines()]
    seqs = content
    PrintDict(DeBruijnKmer(seqs))
