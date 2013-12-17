'''
   Solve the Global Alignment Problem.
   Input: Two protein strings written in the single-letter amino acid alphabet.
   Output: The maximum alignment score of these strings followed by an alignment achieving this maximum score. Use the BLOSUM62 scoring matrix and indel penalty 5
'''
from collections import defaultdict

gap_score = 5

def ReturnScore(amino1, amino2, score):
    if amino1 == "-" or amino2 == "-":
        return 5
    else:
        return score[amino1][amino2]

def ParseMatrix(infile):
    score = defaultdict(lambda: defaultdict(int))
    flag  = 1  #first line flag
    i     = 0
    for line in open(infile):
        content = line.strip().split()
        if flag:
            colnames = content
            flag = 0
            continue
        rowname = colnames[i]
        for j in range(len(colnames)):
            score[rowname][colnames[j]] = int(content[j+1])
        i += 1
    return score

def MaxScore(v, w, i, j, score, backtrack):
    maxscore = -1000
    # v is empty
    newscore = score[i - 1, j] + ReturnScore(v[i - 1], "-")
    if newscore > maxscore:
        backtrack[i, j] =


def GlobalAlign(v, w):
    # v and w are two sequences
    v_len = len(v)
    w_len = len(w)
    score = np.zeros([v_len + 1, w_len + 1])
    for i in range(1, 1 + v_len):
        for j in range(1, 1 + w_len):
            if v[i - 1] == w[j - 1]:


if __name__ == "__main__":
    blosum = "BLOSUM62.txt"
    ParseMatrix(blosum)
