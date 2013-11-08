"""
    Minimun skew for a sequence
"""

def Skew(Seq):
    skew = Seq.count("G") - Seq.count("C")
    return skew

def MinSkew(Seq):
    skewlist = []
    for i in range(len(Seq) + 1):
        skewlist.append(Skew(Seq[:i]))
    minvalue = min(skewlist)
    indexes = [i for i,x in enumerate(skewlist) if x == minvalue]
    print " ".join(map(str,indexes))

def main():
    seq = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    infile = "/home/jing/Downloads/stepic_dataset.txt"
    for each in open(infile):
        seq = each.strip()
    MinSkew(seq)

if __name__ == "__main__":
    main()

