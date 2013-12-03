'''
    Solve the String Reconstruction from Read-Pairs Problem.
    Input: An integer d followed by a collection of paired k-mers PairedReads.
    Output: A string Text with (k, d)-mer composition equal to PairedReads.
'''

class PReads:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __eq__(self, other):
        return other and self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash((self.left, self.right))


def PReadsParser(seqs):
    pass

def PairedReads(seqs, d):
    # node_dict is mapping from number to PReads class
    graph, node_dict = PReadsParser(seqs)
    EulerianPath
    pass

def TestClass():
    first = PReads("A","C")
    second = PReads("D","C")
    third = PReads("A","C")
    print hash(first)
    print hash(second)
    print hash(third)

if __name__ == "__main__":
    TestClass()
