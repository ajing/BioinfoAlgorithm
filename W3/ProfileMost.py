'''
     Input: A string Text, an integer k, and a k*4  matrix Profile.
     Output: A Profile-most probable k-mer in Text.
'''

def Prob(motif, amino_index, matrix):
    motif_len  = len(motif)
    total_prob = 1
    for i in range(motif_len):
        a_index = amino_index.index(motif[i])
        total_prob *= matrix[i][a_index]
    return total_prob

def ProfileMost(seq, k, amino_index, matrix):
    seq_len   = len(seq)
    prob_dict = dict()
    for i in range(seq_len - k + 1):
        motif = seq[i:i + k]
        prob_dict[motif] = Prob(motif, amino_index, matrix)
    minval = max(prob_dict, key = prob_dict.get)
    print minval, prob_dict[minval]

if __name__ == "__main__":
    infile  = "/home/ajing/Downloads/dataset_39_3.txt"
    content = [line.strip() for line in open(infile).readlines()]
    seq     = content[0]
    k       = int(content[1])
    amino_index = content[2].split()
    matrix  = [ map(float, each.split()) for each in content[3:]]
    ProfileMost(seq, k, amino_index, matrix)
