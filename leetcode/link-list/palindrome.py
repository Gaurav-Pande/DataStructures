# Author: Gaurav Pande
# check if a link list is a palindrome or not
# link: https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        t1 = t2 = head

        while t2 and t2.next and t2.next.next:
            t1 = t1.next
            t2 = t2.next.next

        # reverse the list now
        t2 = self.reverse(t1)
        t1 = head

        while t1 and t2:
            if t1.val == t2.val:
                t1 = t1.next
                t2 = t2.next
            else:
                return False
        return True

    def reverse(self, head):
        if head == None or head.next == None:
            return head
        else:
            Node = self.reverse(head.next)
            head.next.next = head
            head.next = None
        return Node

