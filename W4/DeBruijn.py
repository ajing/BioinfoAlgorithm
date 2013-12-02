'''
     Input: An integer k and a string Text.
     Output: DeBruijnk(Text).
'''
from StringComp import StringComp
from OverlapGraph import GraphOverlap

def DeBruijnk(seq, N):
    motif_list = StringComp(seq, N - 1)
    adj_list   = GraphOverlap(motif_list)
    return adj_list

if __name__ == "__main__":
    print DeBruijnk("AAGATTCTCTAC", 4)
