"""
    Reverse complement for sequence
"""

from string import maketrans

def ReverseComplement(Seq):
    ori = "ATCG"
    trans = "TAGC"
    trantab = maketrans(ori, trans)
    Seq.translate(trantab)
    return Seq[::-1]

def FuzzyMatching(Seq1, Seq2, t):
    ## for normal matching
    #return Seq1 == Seq2
    if not len(Seq1) == len(Seq2):
        raise ValueError("length doesn't match for sequence comparison")
    seq_len = len(Seq1)
    mismatch = 0
    for i in range(seq_len):
        if not Seq1[i] == Seq2[i]:
            mismatch += 1
            if mismatch > t:
                return False
    return True

def PatternMatching(Seq, pattern, t):
    seq_len = len(Seq)
    pat_len = len(pattern)
    index_list = []
    for i in range(seq_len - pat_len + 1):
        if FuzzyMatching(Seq[i:i + pat_len], pattern, t):
            index_list.append(i)
    print " ".join(map(str,index_list))
    return index_list

def main():
    infile = "/home/jing/Downloads/stepic_dataset.txt"
    seq = "AAAACCCGGT"
    for each in open(infile):
        seq = each.strip()
    print ReverseComplement(seq)

def mainPM():
    infile = "/home/jing/Downloads/stepic_dataset.txt"
    firstline = 1
    for each in open(infile):
        line = each.strip()
        if firstline:
            pattern = line
            firstline = 0
        else:
            seq = line
    alist = PatternMatching(seq, pattern)
    print alist
    print " ".join(map(str,alist))

def mainFZPM():
    #test case
    #pattern = "ATTCTGGA"
    #seq = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    #t   = 3
    infile = "/home/jing/Downloads/stepic_dataset.txt"
    content = open(infile).readlines()
    pattern, seq, t = content
    PatternMatching(seq.strip(), pattern.strip(),int(t.strip()))


if __name__ == "__main__":
    #main()
    #mainPM()
    mainFZPM()
