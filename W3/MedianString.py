'''
   Input: An integer k, followed by a collection of strings Dna.
   Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern.
'''

import sys
sys.path.append("../W1")
from FrequentWord import PatternGenerator
from MotifEnumeration import AppearInAll

def MedianString(Dna_list, k):
    best_pattern = "A" * k
    patternlist  = []
    score        = dict()
    for eachpattern in PatternGenerator(k):
        if not eachpattern in patternlist:
            if AppearInAll( eachpattern, Dna_list ):
                print eachpattern


if __name__ == "__main__":
    MedianString(["AAAB", "AAAC"], 3)
