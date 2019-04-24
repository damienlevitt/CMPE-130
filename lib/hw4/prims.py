import sys # Library for INT_MAX 


class Graph:

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V
        parent[0] = -1

        for s in range(self.V):
            z = self.find_min(key, mst_set)
            mst_set[z] = True

            for i in range(self.V):
                if 0 < self.graph[z][i] < key[i] and mst_set[i] is False:
                    key[i] = self.graph[z][i]
                    parent[i] = z

    def find_min(self, key, mst_set):
        min = sys.maxsize
        for n in range(self.V):
            if key[n] < min and mst_set[n] is False:
                min = key[n]
                min_key = n
        return min_key
