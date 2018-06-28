# Author: Gaurav Pande
# [https://leetcode.com/problems/add-two-numbers/description/]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""
        head2 = l2
        head1 = l1
        while head1:
            num1 = num1 + str(head1.val)
            head1 = head1.next
        while head2:
            num2 = num2 + str(head2.val)
            head2 = head2.next
        result = str(int(num1[::-1]) + int(num2[::-1]))
        i = len(result) - 2
        head = ListNode(result[len(result) - 1])
        temp = head
        while i >= 0:
            temp.next= ListNode(result[i])
            temp = temp.next
            i = i - 1
        return head
        
        
        
