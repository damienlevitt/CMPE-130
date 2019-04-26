from collections import defaultdict 


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.marked = False

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfshelp(self, v, visited):
        v.marked = True
        for w in self.graph[v]:
            if not w.marked:
                self.dfshelp(w, visited)

    def dfs(self, v):
        visited = [False] * (len(self.graph))
        self.dfshelp(v, visited)

    def bfs(self, v):
        visited = [False] * len(self.graph)
        queue = [v]
        visited[v] = True
        while queue:
            v = queue.pop(0)
            for n in self.graph[v]:
                if not visited[n]:
                    queue.append(n)
                    visited[n] = True
