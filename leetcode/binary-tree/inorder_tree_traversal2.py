# Author: Gaurav Pande
# Inorder tree traversal without recursion and using stack
# Link: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right =  None

def inorder(root):
    result =[]
    stack = []
    if root == None:
        return None
    current_node = root
    done = True
    while done:
        if current_node is not None:
            stack.append(current_node)
            current_node = current_node.left
        else:
            s_top = stack.pop()
            result.append(s_top.val)
            if s_top.right is not None:
                current_node = s_top.right
            elif len(stack)  == 0:
                done = False
    return result

if __name__  == '__main__':
    obj = Node(3)
    obj.left = Node(4)
    obj.right = Node(2)
    obj.left.left = Node(1)
    obj.left.right = Node(6)
    obj.right.left = Node(8)
    obj.right.right = Node(7)

    print (inorder(obj))