from collections import deque


# Instantiable class to represent a graph
class Graph(object):

    # Initializer: given sets of vertices and edges
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

        # Construct an "adjacency list" representation
        self.neighbors = dict()
        for v in vertices:
            self.neighbors[v] = set()
        for v,u in edges:
            self.neighbors[v].add(u)
            self.neighbors[u].add(v)


    def components(self):
        """
        Get a set containing all the components of this graph.
        Each component is a frozenset of vertices.
        :return: a set of the components of the graph.
        """

        # Initialize our sets
        components = set()
        allMarks = set()

        # Iterate through all vertices
        for v in self.vertices:
            # if vertex has not yet been seen
            if v not in allMarks:
                # make new set
                marks = set()
                # run dfs from vertex to new set
                self.dfs(v, marks)
                # bitwise or operation
                allMarks |= marks
                # add marks set to components as frozen set
                components.add(frozenset(marks))

        return components


    def __str__(self):
        """
        String representation method.
        :return: A string description of this graph.
        """

        # Initialize our string
        output = ""

        # go through each vertex and its neighbors
        for v, neighbors in self.neighbors.items():
            # concatenate string values
            output += str(v) + " -> " + str(neighbors) + "\n"

        return output


    def dfs(self, v, marks):
        """
        Depth First Search.
        Add all vertices reachable from v to the marks set.
        :param v: Vertex that we are currently looking at.
        :param marks: the set of vertices we can reach
        """

        # Add the current vertex
        marks.add(v)
        # Iterate through all the possible neighbors
        for u in self.neighbors[v]:
            # If it has not yet been seen, add it to marks
            if u not in marks:
                self.dfs(u, marks)


    def bfs(self, v, parents):
        """
        Breadth First Search.
        Map all vertices to their parents along the shortest path from v.
        :param v: the vertex we are currently at
        :param parents: the parents of that vertex
        """

        # Update parent of v
        parents[v] = v
        # Initialize our frontier
        frontier = deque()
        # Add v to frontier
        frontier.append(v)
        # Until we run out of nodes
        while len(frontier) > 0:
            # Take vertex at front of deque
            p = frontier.popleft()
            # Iterate through its neighbors
            for c in self.neighbors[p]:
                # If it is not a parent
                if c not in parents:
                    # Update front most vertex's parent
                    parents[c] = p
                    # add c to frontier
                    frontier.append(c)

    @staticmethod
    def path(v, parents):
        """

        :param v: current vertex
        :param parents: a list of parents
        :return: Shortest path from to v from root of a BFS tree
        """
        if v in parents:
            path = deque([v])
            while v != parents[v]:
                v = parents[v]
                path.appendleft(v)
            return path


def do_tests():

    # Make sets of vertices and edges
    vertices = {1,2,3,4,5,6,7,8,9}
    edges = {(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(5,9),(6,7),(6,8),(7,8)}

    # Construct the graph
    g = Graph(vertices, edges)
    print(g)

    # See all vertices reachable from 1
    marks = set()
    g.dfs(1, marks)
    print(marks)

    # See all vertices reachable from 6
    marks = set()
    g.dfs(6, marks)
    print(marks)

    # See the BFS tree from 1
    parents = dict()
    g.bfs(1, parents)
    print(parents)

    # Use the BFS tree to find shortest paths from 1
    print(Graph.path(9, parents)) # [1,5,9]
    print(Graph.path(6, parents)) # None

    print(g.components())

if __name__ == '__main__':
    do_tests()
