# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Store the number of level by counting '-'
# in a stack we will add each node.
# we will have to make sure that the stack element are same as the level we are in
# we will get the val if the val is not '-'
# we check if the left node is not empty then we make the new node left of this stack[-] node else
# we make it the right node the if stack[-]
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        i = 0
        stack = []
        while i < len(S):
            level = 0
            val = ""
            while i < len(S) and S[i] == '-':
                stack.append(S[i])
                level += 1
                i += 1
            while i < len(S) and S[i] != '-':
                val += S[i]
                i += 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left:
                stack[-1].right = node
            elif stack:
                stack[-1].left = node
            stack.append(node)
        return stack[0]



