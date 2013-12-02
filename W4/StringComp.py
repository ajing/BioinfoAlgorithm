'''
    Input: An integer k and a string Text.
    Output: Compositionk(Text), where the k-mers are written in lexicographic order.
'''

def StringComp(astring, N):
    string_len  = len(astring)
    print string_len
    string_list = []
    for i in range(string_len - N + 1):
        string_list.append(astring[i:i + N])
    string_list.sort()
    return string_list

if __name__ == "__main__":
    #StringComp("CAATCCAAC", 5)
    infile  = "/home/ajing/Downloads/dataset_51_3.txt"
    content = [line.strip() for line in open(infile).readlines()]
    N       = int(content[0])
    Seq     = content[1]
    print N, Seq
    StringComp(Seq, N)
