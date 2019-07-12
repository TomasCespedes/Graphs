# Author: Tomas Cespedes
# Purpose: backtracking for cliques

from ImplementedGraphs.graph import Graph


# Backtracking algorithm for returning a k-clique in graph
def kclique(graph, k, clique=None):
    """
    Backtracking algorithm for returning a k-clique in grah
    :param graph: the graph we are checking.
    :param k: the size of the clique we want to find.
    :param clique: the clique itself (if found)
    :return: The clique we found if it exists, otherwise nothing
    """
    if clique is None: # Start with an empty path
        return kclique(graph, k, list())

    elif len(clique) == k:
        return clique # Leaf of solution tree

    else: # Inside solution tree

        # Try to extend the path one step
        if len(clique) == 0:
            children = graph.vertices.copy()
        else:
            children = graph.neighbors[clique[-1]].copy()

        # Without repeating any vertices in the path
        for v in clique:
            if v in children:
                children.remove(v)

        # Try each extension
        for c in children:
            if check(clique, c, graph):
                clique.append(c)
                answer = kclique(graph, k, clique)
                if answer is not None:
                    return answer
                else:
                    clique.pop()


def check(clique, vertex, graph):
    """
    Check if a graph is a kclique
    :param clique: a graph that is a clique.
    :param vertex: a vertex.
    :param graph: a graph.
    :return: True if graph is a k-clique otherwise False.
    """
    count = 0
    if len(clique) == 0:
        return True

    for v in clique:
        if vertex in graph.neighbors[v]:
            count = count + 1
            if count == len(clique):
                return True

    return False

# Interactive testing
def run_tests():
    vertices = eval(input("Vertices: "))  # {1, 2, 3, 4, 5}
    edges = eval(input("Edges: "))  # {(1,2), (1,3), (2,4), (2,5), (3,4), (4,5)}
    k = int(input("k: "))  # 3

    graph = Graph(vertices, edges)
    clique = kclique(graph, k)
    print(clique)


if __name__ == '__main__':
    run_tests()