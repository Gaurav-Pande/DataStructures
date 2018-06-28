# Author: Gaurav Pande

# level order traversal in a binary tree using queue
# Link: https://www.geeksforgeeks.org/?p=2686

# Node class to define a node in a binary tree

class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


# define our method here to print element level wise of bfs using queue

from collections import deque
def bfs_print(root):
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        element = queue.popleft()
        result.append(element.val)
        if element.left != None:
            queue.append(element.left)
        if element.right != None:
            queue.append(element.right)
    return result




if __name__ == '__main__':
    obj = Node(3)
    obj.left = Node(4)
    obj.right = Node(2)
    obj.left.left = Node(1)
    obj.left.right = Node(6)
    obj.right.left = Node(8)
    obj.right.right = Node(7)

    result = bfs_print(obj)
    print (result)