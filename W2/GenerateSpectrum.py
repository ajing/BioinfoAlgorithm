'''
    Generate a spectrum for a peptide
'''

Mass_Table = "integer_mass_table.txt"

def AAcidMassParser(infile):
    mass_dict = dict()
    for line in open(infile):
        aacid, mass = line.strip().split()
        mass_dict[aacid] = int(mass)
    return mass_dict

def SubPeptide( peptide, length ):
    # using two concatecated peptide to minic circular peptide
    pep_len = len(peptide)
    newpeptide = peptide + peptide
    sublist = []
    for i in range(pep_len):
        sublist.append(newpeptide[i:i + length])
    return sublist

def PeptideMass(peptide, massdict):
    total = 0
    for each in peptide:
        total += massdict[each]
    return total

def AllPossibleSubPeptide( peptide ):
    pep_len = len(peptide)
    all_possible = [""]
    for i in range(1,pep_len):
        all_possible += SubPeptide(peptide, i)
    all_possible.append(peptide)
    return all_possible

def Cyclospectrum(peptide):
    mass_dict   = AAcidMassParser(Mass_Table)
    subpep_list = AllPossibleSubPeptide(peptide)
    mass_list   = []
    for each in subpep_list:
        mass = PeptideMass(each, mass_dict)
        mass_list.append(mass)
    return sorted(mass_list)

if __name__ == "__main__":
    pepfile = "/home/ajing/Downloads/dataset_20_3.txt"
    peptide = open(pepfile).readlines()[0].strip()
    masslist = Cyclospectrum(peptide)
    print " ".join([str(x) for x in masslist])
