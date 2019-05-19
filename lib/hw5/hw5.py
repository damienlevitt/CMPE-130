import sys

class Graph:
    def __init__(self, verticies):
        self.V = verticies
        self.graph = [[0  for column in range(verticies)]
                      for row in range(verticies)]

    def min_dist(self, dist, sptSet):
        min = sys.maxint
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length

def dijkstra(graph, source):
    dist = [sys.maxint] * sele
    
    return 1

def BellmanFord(graph, source):

    return 1

def Ford_fullerskon(graph, source, sink):    # you can implement Bfs or dfs to get the path from source(start node) to sink(end node)

    return 1 