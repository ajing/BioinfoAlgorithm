'''
Implement TRIEMATCHING to solve the Multiple Pattern Matching Problem.
   Input: A string Text and a collection of strings Patterns.
   Output: All starting positions in Text where a string from Patterns appears as a substring.
'''

from TrieConstruct import BuildTrie

def PrefixTrieMatch(text, trie):
    i = 0  # running index for symbol
    symbol = text[i]
    v = 1  # root of trie
    while True:
        if symbol in trie[v]:
            v = trie[v][symbol]
            i += 1
            try:
                symbol = text[i]
            except:
                symbol = ""
        elif not trie[v]:  # v is the leaf
            return True
        else:
            return False


def TrieMatch(text, trie):
    text_len = len(text)
    matchlist = []
    for i in range(text_len):
        if PrefixTrieMatch(text[i:], trie):
            matchlist.append(str(i))
    print " ".join(matchlist)

def test():
    text = "AATCGGG"
    patterns = ["ATCG", "GGGT"]
    trie = BuildTrie(patterns)
    print PrefixTrieMatch(text, trie)

def main(text, patterns):
    trie = BuildTrie(patterns)
    TrieMatch(text, trie)

if __name__ == "__main__":
    '''
    test()
    '''
    infile   = "/home/ajing/Downloads/dataset_93_6.txt"
    content  = [ x.strip() for x in open(infile).readlines() ]
    text     = content[0]
    patterns = content[1:]
    main(text, patterns)
