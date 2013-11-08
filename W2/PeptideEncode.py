'''
    From peptide, get all subsequence encode that peptide.
'''

from string import maketrans

Codon_Table = "RNA_codon_table_1.txt"

def CodonTableParser(codon_table):
    # return dictionary object map from rna to protein
    protein2rna_dict = dict()
    for eachline in open(codon_table):
        try:
            rna, protein = eachline.strip().split()
        except:
            rna = eachline.strip().split()[0]
            protein = " END "
        if protein in protein2rna_dict:
            protein2rna_dict[protein] += [rna]
        else:
            protein2rna_dict[protein] = [rna]
    return protein2rna_dict

def CartesianProductList( alist, list_append):
    newlist = []
    for eachold in alist:
        for eachnew in list_append:
            newseq = eachold + eachnew
            if not newseq in newlist:
                newlist.append(eachold + eachnew)
    return newlist

def Peptide2DNA(peptide, protein2rnadict ):
    DNAlist = [""]
    for each in peptide:
        codon_coded = protein2rnadict[each]
        dna_codon   = [ RNA2DNA(x) for x in codon_coded ]
        DNAlist = CartesianProductList(DNAlist, dna_codon)
    return DNAlist

def RNA2DNA(rna):
    return rna.replace("U", "T")

def DNA2RNA(dna):
    return dna.replace("T", "U")

def ReverseComplement(seq):
    ori = "ATCG"
    trans = "TAGC"
    trantab = maketrans(ori, trans)
    new_seq = seq.translate(trantab)
    return new_seq[::-1]

def AddReverse(seq_list):
    newlist = []
    for each in seq_list:
        each_rev = ReverseComplement(each)
        if not each_rev in seq_list:
            newlist += [each, each_rev]
        else:
            newlist += [each]
    return newlist

def FindEncodeSubSeq(peptide, seq, p2r_dict):
    subseq_encode = Peptide2DNA(peptide, p2r_dict)
    subseq_encode = AddReverse(subseq_encode)
    all_valid_subseq = []
    subrna_len = len(peptide) * 3
    for i in range(len(seq)):
        subseq = seq[i:i + subrna_len]
        if subseq in subseq_encode:
            all_valid_subseq.append(subseq)
    return all_valid_subseq

def SeqParser(infile):
    # return both sequence and peptide
    return [ eachline.strip() for eachline in open(infile) ]

if __name__ == "__main__":
    seq = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
    peptide = "MA"
    seqfile = "/home/ajing/Downloads/dataset_18_6.txt"
    #seqfile = "/home/ajing/Downloads/test.txt"
    seq, peptide = SeqParser(seqfile)
    p2rdict = CodonTableParser(Codon_Table)
    print "\n".join(FindEncodeSubSeq(peptide, seq, p2rdict))
    print len(FindEncodeSubSeq(peptide, seq, p2rdict))
