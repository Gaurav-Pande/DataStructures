# Author: Gaurav Pande
# delete all the duplicate values from the link list
# link:https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# algo is similar to delete an element from the linklist

import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        dummy = ListNode(-sys.maxsize - 1)
        dummy.next = head
        head = dummy
        temp = dummy.next

        while temp:
            if temp.val == dummy.val:
                dummy.next = temp.next
                temp = temp.next
            else:
                temp = temp.next
                dummy = dummy.next

        return head.next
