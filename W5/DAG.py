'''
Solve the Longest Path in a DAG Problem.
     Input: An integer representing the source node of a graph, followed by an integer representing the sink node of the graph, followed by a list of edges in the graph. The edge notation 0->1:7 indicates that an edge connects node 0 to node 1 with weight 7.
     Output: The length of a longest path in the graph, followed by a longest path.
'''
from collections import defaultdict
import copy

def ParseEdge(edge):
    start, end_c = edge.split("->")
    end, weight  = end_c.split(":")
    return start, end, weight

def ParseGraph(edge_list):
    graph = defaultdict(list)
    all_weight = dict()
    for edge in edge_list:
        start, end, weight = ParseEdge(edge)
        graph[start,"out"].append(end)
        graph[end, "in"].append(start)
        # initialization
        graph[start, "in"]
        graph[end,"out"]
        all_weight[start, end] = float(weight)
    return graph, all_weight

def NoIncommingNodes(graph):
    # help function for TopologicalSorting
    node_list = []
    for eachnode in graph:
        if not graph[eachnode] and eachnode[1] == "in":
            node_list.append(eachnode[0])
    return node_list

def TopologicalSorting(graph):
    # follow the schema on wiki
    graph_c = copy.deepcopy(graph)
    L = []
    S = NoIncommingNodes(graph_c)
    while S:
        n = S.pop()
        L.append(n)
        while graph_c[(n, "out")]:
            m = graph_c[(n, "out")].pop()
            graph_c[(m, "in")].remove(n)
            if not graph_c[(m, "in")]:
                S.append(m)
    return L

def Initialize(graph, order):
    score = dict()
    for each in NoIncommingNodes(graph):
        if each in order:
            score[each] = 0
            order.remove(each)
    return score

def MaxIncoming(score, node, graph, weight, backtrack):
    max_score = 0
    for eachnode in graph[(node, "in")]:
        try:
            new_score = score[eachnode] + weight[(eachnode, node)]
        except:
            print "eachnode:", eachnode, ", node", node
            print graph[(node, "in")]
            raise KeyError()
        if max_score < new_score:
            max_score = new_score
            backtrack[node] = eachnode
    return max_score

def AccessibleNodes(graph, start):
    access = []
    nodeleft = [start]
    while nodeleft:
        nextnode = nodeleft.pop()
        access.append(nextnode)
        child_nodes = graph[nextnode,"out"]
        nodeleft += child_nodes
    return list(set(access))

def Trace(backtrack, start, end):
    track = [end]
    next_node = backtrack[end]
    while next_node:
        track.append(next_node)
        if next_node == start:
            break
        else:
            next_node = backtrack[next_node]
    track.reverse()
    return track

def TrimGraph(graph, accessible):
    for node in accessible:
        newout = [ eachout for eachout in graph[(node, "out")] if eachout in accessible]
        graph[(node, "out")] = newout
        newin = [ eachin for eachin in graph[(node, "in")] if eachin in accessible]
        graph[(node, "in")] = newin

def DAG(graph, start, end, weight):
    accessible = AccessibleNodes(graph, start)
    order = TopologicalSorting(graph)
    order = [x for x in order if x in accessible]
    score = Initialize(graph, order)
    print accessible
    backtrack = dict()
    TrimGraph(graph, accessible)
    for node in order:
        score[node] = MaxIncoming(score, node, graph, weight, backtrack)
    print int(score[end])
    print "->".join(Trace(backtrack, start, end))
    return score, backtrack

def test():
    infile  = "tmp"
    infile  = "/home/ajing/Downloads/dataset_74_7.txt"
    content = [ x.strip() for x in open(infile).readlines() ]
    start   = content[0]
    end     = content[1]
    graph, weight_dict = ParseGraph(content[2:])
    #print NoIncommingNodes(graph)
    #print TopologicalSorting(graph)
    DAG(graph, start, end, weight_dict)

if __name__ == "__main__":
    test()
