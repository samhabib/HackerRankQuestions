"""
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering
properties:

    The value of every node in a node's left subtree is less than the data value of that node.
    The value of every node in a node's right subtree is greater than the data value of that node.

Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has parameter: a pointer to the root of a binary tree. It must return
a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper
functions to complete this challenge.

Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.

Input Format

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its
root node to your function as an argument.

Constraints

0<= data <= 10**4

Output Format

You are not responsible for printing any output to stdout. Your function must return true if the tree is a binary
search tree; otherwise, it must return false. Hidden code stubs will print this result as a Yes or No answer on a new
 line.

"""


"""
My Approach:
I made a recursive function that took into account that we need to keep track of the max and min for each subtree so we
I made checkBSTWithRange and it takes two extra int arguments that are used as comparisons for the rest of the tree.
Other than that it is just a simple recursive check
"""





""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    if root is None or (root.right is None and root.left is None):
        return True
    if root.left is not None and root.right is not None:
        if root.left.data < root.data and root.right.data > root.data:
            return checkBSTWithRange(root.left, root.data, -1) and checkBSTWithRange(root.right, 10 ** 4 + 1, root.data)
        return False
    if root.left is not None:
        if root.left.data < root.data:
            return checkBSTWithRange(root.left, root.data, -1)
        return False
    if root.right is not None:
        if root.right.data > root.data:
            return checkBSTWithRange(root.right, 10 ** 4 + 1, root.data)
        return False


def checkBSTWithRange(root, max, min):
    if root.data >= max or root.data <= min:
        return False

    if root.left is not None and root.right is not None:

        if root.data > root.left.data and root.data < root.right.data:

            return checkBSTWithRange(root.left, root.data, min) and checkBSTWithRange(root.right, max, root.data)
        else:
            return False

    if root.right is not None:

        if root.data < root.right.data:

            return checkBSTWithRange(root.right, max, root.data)
        else:
            return False

    if root.left is not None:

        if root.data > root.left.data:

            return checkBSTWithRange(root.left, root.data, min)
        else:
            return False
    return True