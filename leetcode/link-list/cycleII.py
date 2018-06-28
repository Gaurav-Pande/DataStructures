# Author: Gaurav Pande
# if there is the cycle in a link list, than find the node from where cycle starts
# link: https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        slow = head
        fast = head
        cycle = False
        while fast:
            slow = slow.next
            if fast.next == None or fast.next.next == None:
                return None
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break

        if cycle == False:
            return None
        else:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

        return slow
