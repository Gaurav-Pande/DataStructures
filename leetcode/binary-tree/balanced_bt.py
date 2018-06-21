# check whether a binary tree is a balanced binary tree or not
# link: https://leetcode.com/problems/balanced-binary-tree/description/
#

# Note that the below solution is without recursion

# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# this sol
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        left_subtree = self.getHeight(root.left)
        right_subtree = self.getHeight(root.right)

        if abs(left_subtree - right_subtree) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True

        return False


    # this is not the correct implementation of the height function. It counts number of number of nodes from root to leaves.
    def getHeight(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    # to get the correct height if the tree this should be the function
    def getHeight2(self, root):
        if root == None:
            return -1
        else:
            return 1 + max(self.getHeight2(root.left), self.getHeight2(root.right))



class Solution2(object):
    def isBalanced(self, root):
        return self.check(root) != -1

    def check(self, root):
        if root is None:
            return 0
        l = self.check(root.left)
        r = self.check(root.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)


if __name__  == '__main__':
    obj = Node(3)
    obj.left = Node(4)
    obj.right = Node(2)
    obj.left.left = Node(1)
    #obj.left.left.left =  Node(9)
    #obj.left.right = Node(6)
    #obj.right.left = Node(8)
    #obj.right.right = Node(7)
    ob = Solution2()
    print(ob.check(obj))


