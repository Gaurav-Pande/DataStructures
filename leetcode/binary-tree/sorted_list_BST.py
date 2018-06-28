# Author: Gaurav Pande
# given a sorted link list, build a height balanced binary search tree
# link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # finding middle node in a linked list
        # if odd--> 1,2,3,4,5 than 3 will be root and 1,2 left tree and 4,5 right tree
        # if even --> 1,2,3,4 than 3 will be root and 1,2 left tree and 4 right tree

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        root = TreeNode(temp.val)
        slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)

        return root