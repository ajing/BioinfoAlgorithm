'''
    Translate RNA to protein

'''

Codon_Table = "RNA_codon_table_1.txt"

def CodonTableParser(codon_table):
    # return dictionary object map from rna to protein
    rna2protein_dict = dict()
    for eachline in open(codon_table):
        try:
            rna, protein = eachline.strip().split()
        except:
            rna = eachline.strip().split()[0]
            protein = " END "
        rna2protein_dict[rna] = protein
    return rna2protein_dict

def SeqParser(infile):
    for line in open(infile):
        return line.strip()

def SplitSeq(seq):
    # split sequence as a unit of 3 rna
    num = len(seq)/3
    alist = []
    for i in range(num):
        alist.append(seq[i*3: i*3+3])
    return alist

def TranslateSequence(seq, codon_dict):
    codon_list = SplitSeq(seq)
    protein_list = []
    for each_codon in codon_list:
        protein_list.append(codon_dict[each_codon])
    print "".join(protein_list)

if __name__ == "__main__":
    seq = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    seqfile = "/home/ajing/Downloads/dataset_18_3.txt"
    seq = SeqParser(seqfile)
    print seq
    codondict = CodonTableParser(Codon_Table)
    TranslateSequence(seq, codondict)
