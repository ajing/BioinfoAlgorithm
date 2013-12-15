'''
    To achieve this runtime speedup, you would need to use an efficient data structure in order to maintain the current cycle that Leo is building as well the list of unused edges incident to each node and the list of nodes on the current cycle that have unused edges.
     Input: The adjacency list of an Eulerian directed graph.
     Output: An Eulerian cycle in this graph.
'''

from collections import defaultdict
from random import choice

def RandomWalk(graph_dict, start):
    current = start
    cycle   = [current]
    while True:
        next_points = graph_dict[current]
        next_point = choice(next_points)
        graph_dict[current].remove(next_point)
        if next_point == start:
            break
        current    = next_point
        cycle.append(current)
    return cycle

def ParseGraph(infile):
    content = [line.strip() for line in open(infile).readlines()]
    graph_dict = dict()
    for line in content:
        start, end = line.split(" -> ")
        graph_dict[start] = end.split(",")
    return graph_dict

def EdgesFromGraph(graph_dict):
    edges = []
    for key, value in graph_dict.items():
        if not value:
            continue
        for eachvalue in value:
            edges.append([key, eachvalue])
    return edges

def AvailNodes(cycle, unused_edges):
    avail_nodes = []
    for edge in unused_edges:
        if edge[0] in cycle and not edge[0] in avail_nodes:
            avail_nodes.append(edge[0])
        if edge[1] in cycle and not edge[1] in avail_nodes:
            avail_nodes.append(edge[1])
    return avail_nodes

def RearrangeCycle(cycle, index):
    return cycle[index:] + cycle[:index]

def EulerianCyc(de_graph):
    # debruijn graph is a dictionary
    # graph is a debruijn dictionary
    rand_start    = choice(de_graph.keys())
    current_cycle = RandomWalk(de_graph, rand_start)
    unused_edges  = EdgesFromGraph(de_graph)
    while unused_edges:
        unexplore_node = choice(AvailNodes(current_cycle, unused_edges))
        unexplore_index = current_cycle.index(unexplore_node)
        rearrange_old  = RearrangeCycle(current_cycle, unexplore_index)
        add_cycle = RandomWalk(de_graph, unexplore_node)
        current_cycle = rearrange_old + add_cycle
        unused_edges  = EdgesFromGraph(de_graph)
    return current_cycle

if __name__ == "__main__":
    infile  = "/home/ajing/Downloads/dataset_57_2.txt"
    graph   = ParseGraph(infile)
    cycle   = EulerianCyc(graph)
    index   = cycle.index("1140")
    cycle   = RearrangeCycle(cycle, index)
    cycle.append(cycle[0])
    #print cycle
    print "->".join(cycle)
