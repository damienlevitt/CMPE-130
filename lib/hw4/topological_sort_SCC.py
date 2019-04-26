from collections import defaultdict 
  
# Class to represent a graph


class Graph: 
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def top_sort_helper(self, v, visited, stack):

        visited[v] = True

        for n in self.graph[v]:
            if visited[n] is False:
                self.top_sort_helper(n, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):

        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] is False:
                self.top_sort_helper(i, visited, stack)
