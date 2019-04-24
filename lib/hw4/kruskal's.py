from collections import defaultdict


class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices  # No. of vertices
        self.graph = [] # default dictionary
                        # to store graph

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

        # A function that unions sets x and y

    def union(self, parent, rank, x, y):
        root1 = self.find(parent, x)
        root2 = self.find(parent, y)

        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1

        else:
            parent[root2] = root1
            rank[root1] += 1


    def KruskalMST(self):
        mst = []
        n = 0
        z = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)

        while z < self.V - 1:
            u, v, w = self.graph[n]
            n = n + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                z = z + 1
                mst.append([u, v, w])
                self.union(parent, rank, x, y)
