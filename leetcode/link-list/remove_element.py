# Author: Gaurav Pande
# remove all elements from a  link list with a given val
# link: https://leetcode.com/problems/remove-linked-list-elements/description/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        t1 = ListNode(-1)
        t1.next = head
        t2 = head
        head = t1
        while t2 != None:
            if t2.val == val:
                t1.next = t2.next
                t2 = t2.next
            else:
                t2 = t2.next
                t1 = t1.next
        return head.next


obj = ListNode(1)
obj.next = ListNode(1)

ob = Solution()
head = ob.removeElements(obj,1)

while head != None:
    print (head.val)
    head = head.next