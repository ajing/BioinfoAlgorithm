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

def DrawFigure(xnames, yvalue, errorbar, filename):
    ylen = len(yvalue)
    fig, ax = plt.subplots()
    width   = 1
    ax.bar(np.arange(ylen), yvalue, width, yerr=errorbar)
    num_locator = ylen / 20 if ylen/20 > 0 else 1
    if num_locator < 2:
        plt.xticks(np.arange(ylen) + 0.5, xnames)
    else:
        plt.xticks(np.arange(ylen) + 0.5, xnames)
        myLocator = mticker.MultipleLocator(num_locator)
        ax.xaxis.set_major_locator(myLocator)
    plt.axis('tight')
    plt.setp(ax.get_xticklabels(), rotation='vertical')
    plt.savefig(filename, format = "jpg")
    plt.close()

def SortOrder(s):
    return sorted(range(len(s)), key=lambda k: s[k])

def SeqStat():
    # total length of sequence
    N = 500
    # number of random times
    rand_num = 1000
    for n in range(2, 5):
        # n is the size of pattern
        percent_matrix = np.zeros( (rand_num, 4**n) )
        for t in range(rand_num):
            rand_seq = SeqRandom(N)
            kmerdict = KmerFuzzy(rand_seq, n, 0)
            patterns = kmerdict.keys()
            pattern_frequency = np.array(kmerdict.values())
            pattern_percent   = pattern_frequency * 1.0 / sum(pattern_frequency)
            percent_matrix[t,] = pattern_percent
        # average percent for each pattern
        print percent_matrix.size
        aver_percent = np.mean( percent_matrix, axis = 0)
        print len(aver_percent)
        std_percent = np.std( percent_matrix, axis = 0)
        print len(std_percent)
        percent_order     = SortOrder(aver_percent)
        patterns_reorder  = [ patterns[i] for i in percent_order ]
        percent_reorder = [ aver_percent[i] for i in percent_order ]
        std_reorder     = [ std_percent[i] for i in percent_order ]
        figname = MakeFilename(N,n)
        DrawFigure(patterns_reorder, percent_reorder, std_reorder, figname)

if __name__ == "__main__":
    SeqStat()
