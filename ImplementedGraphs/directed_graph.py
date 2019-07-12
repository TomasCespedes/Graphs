from ImplementedGraphs.graph import Graph
from collections import deque


# Instantiable class to represent a directed graph
class DirectedGraph(Graph):

    # Initializer: given sets of vertices and edges
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

        # Construct an "adjacency list" representation
        self.neighbors = dict()
        for v in vertices:
            self.neighbors[v] = set()
        for v, u in edges:
            self.neighbors[v].add(u)


    def dfs(self, v, newMarks, allMarks=None, order=None):
        """
        Depth First Search implementation
        :param v: Vertices
        :param newMarks: the new vertices that have not been visited yet.
        :param allMarks: All the vertices that have been visited.
        :param order: the order of our graph.
        """

        # Initialize set if needed
        if allMarks is None:
            allMarks = set()

        # Initialize order if needed
        if order is None:
            order = deque()

        # Add the vertices to sets
        newMarks.add(v)
        allMarks.add(v)

        # Go through every neighbor and call function recursively.
        for u in self.neighbors[v]:
            if u not in allMarks:
                self.dfs(u, newMarks, allMarks, order)

        # Add to the front since we traverse tree in reverse order.
        order.appendleft(v)


    def topsort(self):
        """
        Create a topological ordering of verticies
        WARNING: If graph is cyclic, this won't be
        a real ordering
        :return: a list of topological ordering
        """
        marks = set()
        order = deque()
        for v in self.vertices:
            if v not in marks:
                self.dfs(v, set(), marks, order)
        return list(reversed(order))

    def components(self):
        """
        Override the undirected components algorithm.
        Each component is a frozen set of vertices.
        :return: a set of components
        """
        components = set()
        allMarks = set()
        for v in self.reverse().topsort():
            if v not in allMarks:
                marks = set()
                self.dfs(v, marks)
                allMarks |= marks
                components.add(frozenset(marks))
        return components

    def reverse(self):
        """
        Reverse the vertices.
        :return: a DirectedGraph of reversed vertices.
        """
        vertices = {v for v in self.vertices}
        edges = {(v,u) for (u,v) in self.edges}
        return DirectedGraph(vertices, edges)

    def findSource(self):
        """
        Find the source of a graph.
        :return: A vertex in this graph that is a source.
        """

        # Compile all neighbors
        all_neighbors = set()
        for neighbors in self.neighbors.values():
            all_neighbors |= neighbors

        # Find a vertex that isn't a neighbor of anybody
        for v in self.vertices:
            if v not in all_neighbors:
                return v


def do_tests():

    # Make sets of vertices and edges
    vertices = {'A','B','C','D','E','F'}
    edges = {('A','B'),('A','C'),('C','B'),('D','C'),('D','E')}

    # Construct the graph
    g = DirectedGraph(vertices, edges)
    print(g.components())

    # See a topological ordering
    print(g.topsort())


if __name__ == '__main__':
    do_tests()
