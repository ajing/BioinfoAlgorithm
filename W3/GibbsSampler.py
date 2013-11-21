'''
     Input: Integers k, t, and N, followed by a collection of strings Dna.
     Output: The strings BestMotifs resulting from running GIBBSSAMPLER(Dna, k, t, N) with 20 random starts.
'''

def GibbsSampler(dna_list, k, t, N):
    # t: number of sequence
    motifs = random
    best_motifs = motifs
    for i in range(N):
        i = randint(0,t - 1)
        new_motifs = motifs[:i] + motifs[(i + 1):]
        profile = Profile(new_motifs)
        motifs[i] = Motif(profile)
        if ScoreMotifs(motifs) < ScoreMotifs(best_motifs):
            best_motifs = motifs
    return best_motifs

if __name__ == "__main__":
    infile  = "/home/ajing/Downloads/dataset_40_9.txt"
    content = [line.strip() for line in open(infile).readlines()]
    k, t, N    = [int(x) for x in content[0].split()]
    seqs    = content[1:]
    print "\n".join(GibbsSampler(seqs, k, t, N))
