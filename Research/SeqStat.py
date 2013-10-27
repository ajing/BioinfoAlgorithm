"""
    How frequent is significant for a pattern in sequence?
"""
import sys
import numpy as np
sys.path.append("..")
import random
from FrequentWord import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as mticker

def SeqRandom(n):
# random sequence generator
    bases=['A', 'T', 'G', 'C']
    dna_in_list=[]
    while n > 0:
        abase=random.choice(bases)
        dna_in_list.append(abase)
        n=n-1
    return "".join(dna_in_list)

def MakeFilename(N,n):
    return "N_{0}_n_{1}.jpg".format(N,n)

def DrawFigure(xnames, yvalue, filename):
    ylen = len(yvalue)
    mpl.rcParams['xtick.major.pad'] = 8
    fig, ax = plt.subplots()
    ax.bar(np.arange(ylen),yvalue)
    num_locator = ylen / 20 if ylen/20 > 0 else 1
    myLocator = mticker.MultipleLocator(num_locator)
    ax.xaxis.set_major_locator(myLocator)
    plt.xticks(np.arange(ylen) + 0.5, xnames)
    plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
    plt.savefig(filename, format = "jpg")
    plt.close()

def SeqStat():
    # total length of sequence
    N = 1000000
    rand_seq = SeqRandom(N)
    for N in 10**np.arange(1,9):
        for n in range(2,5):
            kmerdict = KmerFuzzy(rand_seq, n, 0)
            patterns = kmerdict.keys()
            pattern_frequency = np.array(kmerdict.values())
            pattern_percent   = pattern_frequency * 1.0 / sum(pattern_frequency)
            figname = MakeFilename(N,n)
            DrawFigure(patterns, pattern_percent, figname)

if __name__ == "__main__":
    SeqStat()
