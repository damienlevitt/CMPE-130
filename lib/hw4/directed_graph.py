class Digraph:
    """This class implements a directed graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph."""
        self.edgeNum = 0
        self.nodeList = set()
        self.parents = dict()
        self.children = dict()

    def add_node(self, node):
        """adds vertices to your graph"""
        if node not in self.nodes:
            self.nodeList.add(node)
            self.parents[node] = dict()
            self.children[node] = dict()
        else:
            return "Node in graph already"

    def add_edge(self, first, last, weight):
        """creates edges between two given vertices in your graph"""
        if first not in self.nodeList:
            self.add_node(first)

        if last not in self.nodeList:
            self.add_node(last)

        self.parents[last][first] = weight
        self.children[first][last] = weight

        self.edgeNum += 1

    def has_edge(self, first, last):   
        """checks if a connection exists between two given nodes in your graph"""
        return first in self.nodeList and last in self.children[first]

    def get_edge_weight(self, first, last):
        """" Returns weight of particular edge from node first to node last """
        return self.children[first][last]

    def remove_edge(self, last, first):
        """removes edges between two given vertices in your graph"""
        del self.parents[last][first]
        del self.children[first][last]
        self.edgeNum -= 1

    def remove_node(self, node):
        """removes vertices from your graph"""
        if node not in self.nodeList:
            print("Node not in graph, unable to delete")
            return
        self.edgeNum -= len(self.parents[node]) + len(self.children[node])

        # Deletes link to parent
        for link1 in self.parents[node]:
            del self.children[link1][node]

        # Deletes link to Child
        for link2 in self.children[node]:
            del self.parents[link2][node]

        # Deletes nodes from dictionaries
        del self.parents[node]
        del self.children[node]
        self.nodeList.remove(node)

    def contains(self, node):
        """checks if your graph contains a given value"""
        return node in self.nodes

