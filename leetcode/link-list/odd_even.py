# given a link list, separate the odd and even part of the list and combine
# link: https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = d1 = ListNode(0)
        dummy2 = d2 = ListNode(0)
        c = 1
        while head:
            if c % 2 != 0:
                dummy2.next = head
                head = head.next
                dummy2 = dummy2.next
                c += 1
            else:
                dummy1.next = head
                head = head.next
                dummy1 = dummy1.next
                c += 1
        dummy2.next = d1.next
        head = d2.next
        dummy1.next = None

        return head
