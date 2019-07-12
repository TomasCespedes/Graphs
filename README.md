# Graphs
  In this repository there are some common implementations for sets of objects connected together in some manner known as graphs. The three that I have implemented are directed graph, a weighted graph, and a normal graph. These can be found within the ImplementedGraphs directory. Each "node" is considered a vertex and they are connected to other nodes by edges. If one vertex is connected to another then they are considered neighbors. In the examples folder, there are some examples that will be explained that utilize the graphs and other data structures to solve specific problems. 
  
## Implemented Graphs
### Graph
  The first graph that is implemented is just a regular graph that is depicted as a dictionary of neighbors where the vertex is the key and it's value is a set of it's neighbors. We want to use a set here because the order does not matter and we can locate items in constant time. The Graph class has depth first search implemented which adds all vertices reachable from any vertex to a "marks" set. It also has breadth first search which maps all vertices to their parents along the shortest path from any vertex.

### Directed Graph
  The difference between a directed graph and a regular graph is that the directed graph has a direction to it. So if a vertex U has a neighbor V, that does not ensure that V has the neighbor U. The directed graph class also has a depth first search implementation. Since we have a direction, we can implement a topsort algorithm which returns a topolgocial ordering of vertices. An example of a topological sort can be found below. A directed graph can also be reversed which is simply just switching keys and the values in the dictionary. Since we have a direction, it can be useful for some problems to find where the root node is which is also implemented. An example of a directed graph can be found below.
  
   
 <p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/35609863/61159886-99f81700-a4cb-11e9-81af-43d904293701.png">
</p>
 
### Weighted Graph
  A weighted graph is a graph that does not have direction, but has values over each edge. Since each neighbor share one edge, the weight from vertex U to vertex V is the same as from V to U. The weighted graph class has Dijkstra's algorithm implemented which finds the least cost path from V to its parents. In addition to Dijkstra's, Prim's is also a part of the weighted graph class. Prim's algorithm finds the minimum spanning tree but it is greedy. As a result, it sometimes goes over the same vertex more than once and we lose some computational efficency. An example of a weighted graph can be found below.   

  ![image](https://user-images.githubusercontent.com/35609863/61159908-b09e6e00-a4cb-11e9-9b66-b44f2a024d95.png =250x250)

  
## Examples
The examples contains huffmanTree.py, kclique.py, and transform.py. The Huffman Tree is implemented within the first file which builds a huffman tree based on given frequency inputs. The second file ultizes the normal graph implementation which finds if a certain graph has a clique of k size and returns True or False. The third file is a words transformer which if the user inputs a source word and a target word, it takes the user through the steps of changing that source word to the input word. This only works if both words are real words. 
