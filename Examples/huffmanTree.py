# Author: Tomas Cespedes
# Purpose: Huffman coding
# Citations:

from heapq import heappush, heappop

class HuffmanTree(object):

    # Constructor
    def __init__(self, char, left, right):
        """
        :param char: The label of this node (only leaves need labels)
        :param left: the left child of this node (only non-leaves need children)
        :param right:  the right child of this node (only non-leaves need children)
        """
        self.char = char
        self.left = left
        self.right = right


    def __lt__(self, other):
        """
        Needed because HuffmanTrees will get compared if their priorities tie
        Doesn't matter how we break the tie, just that we make them comparable
        :param other: other HuffmanTree
        :return: true
        """
        return True


    def display(self, prefix=""):
        """
        Print the character encoding represented by this tree
        :param prefix: how all codes in this tree begin
        :return: Nothing
        """
        # create tree
        treeDict = dict()

        # if left side is not empty
        if (self.left != None):
            # add a 0 place holder
            self.left.display(prefix + "0")
        # else add empty spot
        else:
            treeDict[self.char] = prefix
        # if right side is not empty
        if (self.right != None):
            # add a 1 place holder
            return self.right.display(prefix + "1")
        # else add empty spot
        else:
            treeDict[self.char] = prefix

        for y in treeDict:
            print(str(y) + ", " + treeDict[y])

    @staticmethod
    def encode(frequencies):
        """
        Build and return a Huffman tree based on our input
        :param frequencies: mapping of characters to frequencies
        :return: a Huffman Tree
        """
        q = list()
        for x in frequencies:
            tree = HuffmanTree(x, None, None)
            heappush(q, (frequencies[x], tree))
        while len(q) > 1:
            freq1, tree1 = heappop(q)
            freq2, tree2 = heappop(q)
            tree3 = HuffmanTree(None, tree1, tree2)
            heappush(q, (freq1 + freq2, tree3))
        r1, r2 = heappop(q)
        return r2

# Interactive testing
def test():
    # Type them like {'a':70, 'c':3, 'g':20, 't':37}
    frequencies = eval(input("Frequencies: "))
    HuffmanTree.encode(frequencies).display()


if __name__ == '__main__':
    test()