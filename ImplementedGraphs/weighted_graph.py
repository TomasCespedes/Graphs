# Author: Tomas Cespedes

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


    def __str__(self):
        """
        String method for class.
        :return: A string description of this graph.
        """
        output = ""
        for v, neighbors in self.neighbors.items():
            neighbors = {u: self.weights[(v, u)] for u in neighbors}
            output += str(v) + " -> " + str(neighbors) + "\n"
        return output


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

        # Initialize the vertex
        parents[v] = v
        # Has cost of 0
        costs[v] = 0
        # Add to frontier
        frontier = [(0, v)]
        # Create an off frontier set
        off_frontier = set()
        # Do this until there are items left in frontier
        while len(frontier) > 0:
            # Get cost and the node
            pcost, p = heappop(frontier)
            # If it has not yet been seen
            if p not in off_frontier:
                # add to off frontier
                off_frontier.add(p)
                # check all it's neighbors
                for c in self.neighbors[p]:
                    # cost to node's neighbors
                    w = pcost + self.weights[(p, c)]
                    # update if cost is less or if cost has not yet been seen
                    if c not in costs or w < costs[c]:
                        # update dictionaries
                        parents[c] = p
                        costs[c] = w
                        # push onto frontier
                        heappush(frontier, (w, c))

    def prim(self, v, parents):
        """
        Prim's Algorithm.
        :param v: A vertex.
        :param parents: The parents of the vertex.
        :return:
        """

        # Initialize our parents dictionary with vector
        parents[v] = v
        # create frontier
        frontier = [(0, v)]
        # create finished set
        finished = set()
        # while there are items in frontier
        while len(frontier) > 0:
            # get current cost and vertex
            c, current = heappop(frontier)
            # add to the finished set
            finished.add(current)
            # go through all neighbors
            for i in self.neighbors[current]:
                # if they have not yet been visited
                if i not in finished:
                    # get weight for current vertex
                    w = self.weights[(current, i)]
                    # if it is not in the finished set
                    if i not in finished:
                        # update current vertex
                        parents[i] = current
                        # push onto frontier with weight
                        heappush(frontier, (w, i))
                    # if cost is greater than weight
                    if c > w:
                        # update dictionaries
                        parents[i] = current
                        # push onto frontier
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
