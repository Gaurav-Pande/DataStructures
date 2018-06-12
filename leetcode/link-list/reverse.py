# reverse a link list using recursion
# Link: https://leetcode.com/problems/reverse-linked-list/description/



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head, val):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            Node = self.reverseList(head.next,head.next.val)
            head.next.next = head
            head.next = None

        return Node




if __name__ == '__main__':
    obj = ListNode(1)
    obj.next = ListNode(2)
    obj.next.next = ListNode(3)
    obj.next.next.next = ListNode(4)
    obj.next.next.next.next = ListNode(5)
    obj.next.next.next.next.next = ListNode(6)
    ob = Solution()
    head = ob.reverseList(obj,obj.val)
    while head:
        print (head.val)
        head = head.next