# Author: Tomas Cespedes
# Worked With: Taylor Digilio
# Purpose: Update Prim's

from heapq import *
from ImplementedGraphs.graph import Graph


class WeightedGraph(Graph):
    # Initializer: given sets of vertices and edges
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

        # Construct an "adjacency list" representation
        self.neighbors = dict()
        for v in vertices:
            self.neighbors[v] = set()
        for u, v, w in edges:
            self.neighbors[v].add(u)
            self.neighbors[u].add(v)

        # Allow for fast lookup of edge weights
        self.weights = dict()
        for u, v, w in edges:
            self.weights[(u, v)] = w
            self.weights[(v, u)] = w

    # Return a string description of this graph
    def __str__(self):
        output = ""
        for v, neighbors in self.neighbors.items():
            neighbors = {u: self.weights[(v, u)] for u in neighbors}
            output += str(v) + " -> " + str(neighbors) + "\n"
        return output

    # Map all vertices to their parents along the lowest-weight
    # path from v. Also Map all vertices to their costs
    # along that same path
    def dijkstra(self, v, parents, costs):
        """
        Dijkstra's Algorithm
        Map all vertices to their parents along the lowest-weight
        path from v. Also map all vertices to their costs along
        the same path.
        :param v: A vertex.
        :param parents: The parents of that vertex.
        :param costs: The cost to get to that vertex.
        """
        parents[v] = v
        costs[v] = 0
        frontier = [(0, v)]
        off_frontier = set()
        while len(frontier) > 0:
            pcost, p = heappop(frontier)
            if p not in off_frontier:
                off_frontier.add(p)
                for c in self.neighbors[p]:
                    w = pcost + self.weights[(p, c)]
                    if c not in costs or w < costs[c]:
                        parents[c] = p
                        costs[c] = w
                        heappush(frontier, (w, c))

    def prim(self, v, parents):
        """
        Prim's Algorithm.
        :param v: A vertex.
        :param parents: The parents of the vertex.
        :return:
        """

        parents[v] = v
        frontier = [(0, v)]
        finished = set()
        while len(frontier) > 0:
            c, current = heappop(frontier)
            finished.add(current)
            for i in self.neighbors[current]:
                if i not in finished:
                    w = self.weights[(current, i)]
                    if i not in finished:
                        parents[i] = current
                        heappush(frontier, (w, i))
                    if c > w:
                        parents[i] = current
                        heappush(frontier, (w, i))


def do_tests():
    # Make sets of vertices and edges
    vertices = {'A', 'B', 'C', 'D', 'E'}
    edges = {('A', 'B', 4), ('A', 'C', 2),
             ('B', 'C', 1), ('B', 'D', 3),
             ('C', 'E', 6), ('D', 'E', 1)}

    # Construct the graph
    g = WeightedGraph(vertices, edges)
    print(g)


    parents = dict()
    costs = dict()
    print(parents)
    g.prim('A', parents)
    print(parents)

    (Graph.path('B', parents), costs['B'])
    print(Graph.path('E', parents), costs['E'])

if __name__ == '__main__':
    do_tests()
