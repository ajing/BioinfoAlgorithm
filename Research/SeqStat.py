"""
    How frequent is significant for a pattern in sequence?
"""
import random
from FrequentWord import *

def SeqRandom(n):
# random sequence generator
    bases=['A', 'T', 'G', 'C']
    dna_in_list=[]
    while n > 0:
        abase=random.choice(bases)
        dna_in_list.append(abase)
        n=n-1
    return "".join(dna_in_list)

def SeqStat():
    # total length of sequence
    N = 10000
    rand_seq = SeqRandom(N)
    for n in range(2,10):
