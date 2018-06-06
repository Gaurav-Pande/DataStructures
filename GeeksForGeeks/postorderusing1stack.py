# Iterative post order traversal in a binary tree using 1 stacks
# Link: https://www.geeksforgeeks.org/iterative-postorder-traversal/

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def postOrderTraversal(root):
    stack1 = []

    stack1.append(root)

    while stack1:
        element = stack1[-1]

    return  None