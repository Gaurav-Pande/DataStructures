# Author: Gaurav Pande
# inroder traversal of a binary tree using a single stack.
# link:

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):

    if root == None:
        return  None

    current = root
    stack = []
    dummynode = Node(-1)
    stack.append(dummynode)
    result = []
    while current != None or stack != None:
        if current != None:
            stack.append(current)
            current = current.left
        else:
            temp = stack.pop()
            result.append(temp.val)

            if temp.val == -1:
                result.pop()
                break

            if temp.right != None:
                current = temp.right
    return result


if __name__  == '__main__':
    obj = Node(1)
    obj.left = Node(2)
    obj.right = Node(2)
    obj.left.left = Node(4)
    obj.left.right = Node(5)
    obj.right.left = Node(3)
    obj.right.right = Node(7)

    print (inorder_traversal(obj))

