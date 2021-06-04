# Binary tree:
# A binary tree is a tree-type non-linear data structure with a maximum of two children for each parent.
# Every node in a binary tree has a left and right reference along with the data element.
# Tree:
#       20
#      /  \
#     15   16
#     / \    \
#    5   12  22
#   /
#   2

import random


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def createTree():
    print("The tree was created!")
    pass


def addNode():
    print("The node was added!")
    pass


def deleteNode():
    print("The node was deleted!")
    pass


def seachNode():
    print("Your target is: ")
    pass


if __name__ == '__main__':
    tree_size = int(input('What will be the size of your tree? '))

    tuple = (random.randint(0, 50) for i in range(tree_size))

    newTree = createTree(tuple)
    print("==============================================")
    print("\n")
    newNode = addNode(tuple)
    print("==============================================")
    print("\n")
    popNode = deleteNode(tuple)
    print("==============================================")
    print("\n")
    findNode = seachNode(tuple)
