'''
    Cyclopeptide sequencing with branch and bound
'''

from GenerateSpectrum import *

massdict = AAcidMassParser(Mass_Table)
MASSLIST = sorted(list(set(massdict.values())))

def Expand(candlist):
    # candlist is a list of amino acids mass candidate list
    # like [[1,3,2], [4,2,1]]
    new_list = []
    if candlist == [0]:
        for eachmass in MASSLIST:
            new_list.append([eachmass])
        return new_list
    for each in candlist:
        for eachmass in MASSLIST:
            newitem = [eachmass] + each
            if not newitem in new_list:
                new_list.append(newitem)
            newitem = each + [eachmass]
            if not newitem in new_list:
                new_list.append(newitem)
    return new_list

def CheckDuplicate(alist):
    for each in alist:
        if alist.count(each) > 1:
            print "Yes duplicates!"
    print "no duplicates"

def Consistent(masslist, spectrum):
    mass_spectrum = Cyclospectrum(masslist)
    for each in mass_spectrum:
        if not each in spectrum:
            return False
    return True

def MassEqual(spectrum1, spectrum2):
    pass

def Cyclospectrum(aacid_mass_list):
    mass_combine = AllPossibleSubPeptide(aacid_mass_list)
    mass_combine = [x for x in mass_combine]
    mass_sum     = [sum(x) for x in mass_combine]
    mass_sum     = list(set(mass_sum))
    return sorted(mass_sum)

def CyclopeptideSequencing(spectrum_list):
    candidates = [0]
    outputlist = []
    while candidates:
        print len(candidates)
        candidates = Expand(candidates)
        print len(candidates)
        candidates_new = []
        for peptide in candidates:
            if Cyclospectrum(peptide) == spectrum_list:
                outputlist.append(peptide)
            elif Consistent(peptide, spectrum_list):
                candidates_new.append(peptide)
        candidates = candidates_new
        print candidates
    return outputlist

if __name__ == "__main__":
    massfile = "/home/ajing/Downloads/dataset_22_4.txt"
    masslist = open(massfile).readlines()[0].strip().split()
    #masslist = [0,113,128,186,241,299,314,427]
    masslist = "0 71 97 99 103 113 113 114 115 131 137 196 200 202 208 214 226 227 228 240 245 299 311 311 316 327 337 339 340 341 358 408 414 424 429 436 440 442 453 455 471 507 527 537 539 542 551 554 556 566 586 622 638 640 651 653 657 664 669 679 685 735 752 753 754 756 766 777 782 782 794 848 853 865 866 867 879 885 891 893 897 956 962 978 979 980 980 990 994 996 1022 1093".split()
    masslist = map( int, masslist )
    print masslist
    peptidelist = CyclopeptideSequencing(sorted(masslist))
    print " ".join([ "-".join(map(str, peptide)) for peptide in peptidelist])
