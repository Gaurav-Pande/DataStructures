# Iterative post order traversal in a binary tree using 2 stacks
# Link: https://www.geeksforgeeks.org/iterative-postorder-traversal/

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



def postOrderTraversal(root):
    stack1 = []
    stack2 = []
    result = []
    stack1.append(root)

    if root == None:
        return None

    while stack1:
        element = stack1.pop()
        stack2.append(element)
        if element.left != None:
            stack1.append(element.left)
        if element.right != None:
            stack1.append(element.right)

    while stack2:
        result.append(stack2.pop().val)
    return result


if __name__  == '__main__':
    obj = Node(1)
    obj.left = Node(2)
    obj.right = Node(3)
    obj.left.left = Node(4)
    obj.left.right = Node(5)
    obj.right.left = Node(6)
    obj.right.right = Node(7)

    print(postOrderTraversal(obj))
