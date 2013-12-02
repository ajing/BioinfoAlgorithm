'''
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.
'''

def CompareSeq(seq1, seq2):
    if seq1[1:] == seq2[:-1]:
        return True
    else:
        return False

def GraphOverlap(seqs):
    num_seqs = len(seqs)
    adj_list = []
    for i in range(num_seqs - 1):
        for j in range(i + 1, num_seqs):
            if CompareSeq(seqs[i], seqs[j]):
                adj_list.append([seqs[i], seqs[j]])
            if CompareSeq(seqs[j], seqs[i]):
                adj_list.append([seqs[j], seqs[i]])
    adj_list = sorted(adj_list, key = lambda k: k[0])
    return adj_list


if __name__ == "__main__":
    #seqstring = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]
    #infile  = "/home/ajing/Downloads/overlap_graph_1.txt"
    infile  = "/home/ajing/Downloads/dataset_52_7.txt"
    content = [line.strip() for line in open(infile).readlines()]
    seqstring = content
    adjlist = GraphOverlap(seqstring)
    print "\n".join([" -> ".join(x) for x in adjlist])

