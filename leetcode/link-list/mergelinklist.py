# Merge two sorted list
# link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        temp_node = n1 = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                n1.next = l1
                l1 = l1.next
            else:
                n1.next = l2
                l2 = l2.next
            n1 = n1.next

        if l1 == None:
            n1.next = l2
        else:
            n1.next = l1

        return temp_node.next





