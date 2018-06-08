# Iterative post order traversal in a binary tree using 1 stacks
# Link: https://www.geeksforgeeks.org/iterative-postorder-traversal/
# video tutorial to follow: https://www.youtube.com/watch?v=xLQKdq0Ffjg

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def postOrderTraversal(root):
    stack1 = []
    result = []
    current  = root
    while stack1 or current:
        if current != None:
            stack1.append(current)
            current = current.left
        else:
            temp = stack1[-1].right
            if temp == None:
                temp = stack1.pop()
                result.append(temp.val)
                while stack1 and temp == stack1[-1].right:
                    temp = stack1.pop()
                    result.append(temp.val)
            else:
                current = temp



    return  result



if __name__  == '__main__':
    obj = Node(3)
    obj.left = Node(4)
    obj.right = Node(2)
    obj.left.left = Node(1)
    obj.left.right = Node(6)
    obj.right.left = Node(8)
    obj.right.right = Node(7)

    print(postOrderTraversal(obj))