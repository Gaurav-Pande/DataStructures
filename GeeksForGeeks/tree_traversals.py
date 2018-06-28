# Author: Gaurav Pande
# preorder posrorder and inorder traversal in a binary tree
# Link: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


# Define a Node for tree

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# inorder traversal in a binary tree
def inorder(root,result):
    if root == None:
        return None
    else:
        inorder(root.left,result)
        result.append(root.val)
        inorder(root.right,result)
    return result



def postorder(root,result=[]):
    if root == None:
        return None
    else:
        postorder(root.left,result)
        postorder(root.right,result)
        result.append(root.val)
    return result



def preorder(root,result):
    if root == None:
        return None
    else:
        result.append(root.val)
        preorder(root.left,result)
        preorder(root.right,result)
    return result





if __name__ == '__main__':
    obj = Node(3)
    obj.left = Node(4)
    obj.right = Node(2)
    obj.left.left = Node(1)
    obj.left.right = Node(6)
    obj.right.left = Node(8)
    obj.right.right = Node(7)
    print (preorder(obj,result=[]))
    print (postorder(obj))
    print (inorder(obj,result=[]))