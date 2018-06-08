# partition a LinkList based on a value
# link: https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        d1 = l1 = ListNode(0)
        d2 = l2 = ListNode(0)

        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next

        l2.next = None
        l1.next = d2.next

        return d1.next


obj = ListNode(1)
obj.next = ListNode(4)
obj.next.next = ListNode(3)
obj.next.next.next = ListNode(2)
obj.next.next.next.next = ListNode(5)
obj.next.next.next.next.next = ListNode(2)

ob = Solution()
head = ob.partition(obj,3)
while head:
    print (head.val)
    head = head.next