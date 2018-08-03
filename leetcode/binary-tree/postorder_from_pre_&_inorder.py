# Author: Gaurav Pande
# print postorder traversal from inorder and preorder traversal

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def BuiltTree(inorder, preorder):
    if not inorder or not preorder:
        return  None

    root = Node(preorder.pop(0))
    inorder_index = inorder.index(root.val)

    root.left = BuiltTree(inorder[:inorder_index],preorder)
    root.right = BuiltTree(inorder[inorder_index + 1:], preorder)

    return root

def printPostorder(root):
    if root == None:
        return None
    else:
        printPostorder(root.left)
        printPostorder(root.right)
        print (root.val)

if __name__ == '__main__':
    inorder = [4, 2, 5, 1, 3, 6]
    preorder = [1, 2, 4, 5, 3, 6]
    root  = BuiltTree(inorder,preorder)
    #print (root.val)
    #printPostorder(root)