'''
     Input: The adjacency list of a directed graph that has an Eulerian path.
     Output: An Eulerian path in this graph.
'''

from EulerianCyc import ParseGraph, EulerianCyc, RearrangeCycle

def FindStartEnd(graph):
    out_num = dict()
    in_list = []
    for key, value in graph.items():
        out_num[key] = len(value)
        in_list += value
    all_nodes = list(set(in_list + out_num.keys()))
    for node in all_nodes:
        if not node in out_num:
            end = node
            continue
        if out_num[node] > in_list.count(node):
            start = node
        if out_num[node] < in_list.count(node):
            end = node
    return start, end

def IndexFakePath(circle, start, end):
    circle_len = len(circle)
    for i in range(circle_len):
        if end == circle[i] and start == circle[i+1]:
            return i + 1
    raise "Something wrong with finding the index of fake path"

def JoinPathtoString(path):
    partlist = [x[-1] for x in path]
    return path[0][:-1] + "".join(partlist)

def EulerianPath(graph):
    start, end = FindStartEnd(graph)
    # make debruijn graph for graph
    if end in graph:
        graph[end].append(start)
    else:
        graph[end] = [start]
    cycle      = EulerianCyc(graph)
    start_index= IndexFakePath(cycle, start, end)
    cycle      = RearrangeCycle(cycle, start_index)
    return cycle

if __name__ == "__main__":
    infile  = "/home/ajing/Downloads/dataset_57_6.txt"
    graph   = ParseGraph(infile)
    #print FindStartEnd(graph)
    path    = EulerianPath(graph)
    print JoinPathtoString(path)
