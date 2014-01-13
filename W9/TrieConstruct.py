'''
Solve the Trie Construction Problem.
     Input: A collection of strings Patterns.
     Output: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the integers labeling the initial and terminal nodes of the edge, respectively; the third member of the triple must be the symbol labeling the edge.
'''

def PrintTrie(trie):
    for i in range(len(trie)):
        for eachc in trie[i]:
            print i, trie[i][eachc], eachc

def BuildTrie(patterns):
    trie = [{}, {}] # a list of dictionary contain the trie structure
    id_inc = 2
    for eachp in patterns:
        startnode = 1
        for eachc in eachp:
            if eachc in trie[startnode]:
                startnode = trie[startnode][eachc]
            else:
                trie[startnode][eachc] = id_inc
                trie.append({})
                startnode = id_inc
                id_inc += 1
    return trie

if __name__ == "__main__":
    content = "GGTA\nCG\nGGC"
    patterns = content.split()
    #content = "GGCA"
    infile   = "/home/ajing/Downloads/dataset_93_3.txt"
    patterns = [ x.strip() for x in open(infile).readlines()]
    #patterns.sort()
    #print patterns
    trie = BuildTrie(patterns)
    PrintTrie(trie)
