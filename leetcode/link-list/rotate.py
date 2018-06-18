# rotate a link list
# link: https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        t1 = t2 = head
        l = 1
        if head == None or head.next == None:
            return head
        while t1.next != None:
            l += 1
            t1 = t1.next
        if k >= l:
            len_to_travel = l - k % l
        else:
            len_to_travel = l - k

        if len_to_travel == 0:
            return head
        else:
            while len_to_travel > 1:
                t2 = t2.next
                len_to_travel -= 1
            t1.next = head
            head = t2.next
            t2.next = None

        return head

