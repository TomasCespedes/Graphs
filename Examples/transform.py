# Author: Tomas Cespedes
# Purpose: transform words from one real word to any other real word
# Citations:
from ImplementedGraphs.graph import Graph

# Read in the words
words = set(open("words", "r").read().split())

# Start some sets (since searching through sets is fastest)
vertices = set()
edges = set()

# Initialize our alphabet dictionary
alphabetdictionary = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
                      '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j',
                      '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o',
                      '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't',
                      '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y',
                      '26': 'z'}



# Make each word a vertex
while len(words) > 0:

    # Get random word from words file
    word = words.pop()
    # save the word as a list
    temp_word = list(word)
    # add word in vertices
    vertices.add(word)

    # Go through each letter in the world
    for letter in range(len(temp_word)):

        # Iterate through each letter of alphabet
        for c in alphabetdictionary.values():
            # Change temp word letter by each character
            temp_word[letter] = c
            # create a string from new word
            new_word = ''.join(temp_word)

            # If the new word is a real word
            if new_word in words:
                # Add it to a list of vertices
                vertices.add(new_word)
                # connect it to original word as a neighbor
                edges.add((word, new_word))

        temp_word = list(word)
print("Number of Connected Edges: " + str(len(edges)))
print("Connected Edges: " + str(edges))


# Construct the graph
wordGraph = Graph(vertices, edges)

# Transform words
while True:


    # Ask user to input a source word
    source = input("Source word: ")

    # If it is not a real word, respond accordingly
    if source not in vertices:
        print("Unknown word:", source, "\n")
        continue

    # Ask user to input a target word
    target = input("Target word: ")

    # If it is not a real word, respond accordingly
    if target not in vertices:
        print("Unknown word:", target, "\n")
        continue

    # Find a shortest path from source word to target word
    parents = dict()

    # Run Breadth first search
    wordGraph.bfs(source, parents)

    # Print resulting graph
    print(Graph.path(target, parents))

