import sys
from collections import defaultdict


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

    def dijkstra(self, source):
        dist = [sys.maxint] * self.V
        dist[source] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

    def BellmanFord(self, source):
        dist = [float("Infinite")] * self.V
        dist[source] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Infinite") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Infinite") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

    def Ford_fullerskon(graph, source, sink):    # you can implement Bfs or dfs to get the path from source(start node) to sink(end node)
        def __init__(self, graph):
            self.graph = graph  # residual graph
            self.ROW = len(graph)
            # self.COL = len(gr[0])

        '''Returns true if there is a path from source 's' to sink 't' in 
        residual graph. Also fills parent[] to store the path '''

        def BFS(self, s, t, parent):

            visited = [False] * (self.ROW)

            queue = []

            queue.append(s)
            visited[s] = True

            while queue:
                u = queue.pop(0)
                for ind, val in enumerate(self.graph[u]):
                    if visited[ind] == False and val > 0:
                        queue.append(ind)
                        visited[ind] = True
                        parent[ind] = u

            return True if visited[t] else False

        def FordFulkerson(self, source, sink):
            parent = [-1] * (self.ROW)
            max_flow = 0  # There is no flow initially
            while self.BFS(source, sink, parent):
                path_flow = float("Infinite")
                s = sink
                while (s != source):
                    path_flow = min(path_flow, self.graph[parent[s]][s])
                    s = parent[s]
                max_flow += path_flow
                v = sink
                while (v != source):
                    u = parent[v]
                    self.graph[u][v] -= path_flow
                    self.graph[v][u] += path_flow
                    v = parent[v]

            return max_flow
