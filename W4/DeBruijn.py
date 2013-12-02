'''
     Input: An integer k and a string Text.
     Output: DeBruijnk(Text).
'''
from StringComp import StringComp
from OverlapGraph import GraphOverlap
from collections import defaultdict

def DeBruijnk(seq, N):
    motif_list    = StringComp(seq, N - 1)
    adj_list      = GraphOverlap(motif_list)
    collapse_dict = defaultdict(list)
    for start, end in adj_list:
        collapse_dict[start].append(end)
    return collapse_dict

def PrintDict(col_dict):
    col_sets = col_dict.items()
    col_list = [list(x) for x in col_sets]
    col_list = sorted(col_list, key = lambda k: k[0])
    for each in col_list:
        print each[0]

if __name__ == "__main__":
    print DeBruijnk("AAGATTCTCTAC", 4)
