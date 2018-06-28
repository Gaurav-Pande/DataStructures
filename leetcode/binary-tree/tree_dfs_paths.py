# in a binary tree find the tree paths from root to leave
# link:https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# we can solve this problem using recursion and preorder traversal
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is not None:
            return self.runDFS(root,"",[])

    def runDFS(self,root,path,result):
        if root.left is None and root.right is None:
            path += str(root.val)
            result.append(path)
        if root.left is not None:
            self.runDFS(root.left,path + str(root.val) + "=>",result)
        if root.right is not None:
            self.runDFS(root.right,path + str(root.val) + "=>",result)
        return result


if __name__  == '__main__':
    obj = TreeNode(1)
    obj.left = TreeNode(2)
    obj.right = TreeNode(2)
    obj.left.left = TreeNode(3)
    obj.left.right = TreeNode(4)
    obj.right.right = TreeNode(3)

    ob = Solution()
    print(ob.binaryTreePaths(obj))
