# Author: Gaurav Pande
# reorder a list
# link : https://leetcode.com/problems/reorder-list/submissions/1
 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import math


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        t = head
        stack = []
        flag = True
        if head == None or head.next == None:
            flag = False

        if flag:
            while t:
                stack.append(t)
                t = t.next
            t1 = head
            t2 = head.next
            s = math.floor(len(stack) / 2)

            while s > 0:
                elem = stack.pop()
                t1.next = elem
                elem.next = t2
                t1 = t1.next.next
                t2 = t2.next
                s -= 1

            if len(stack) % 2 == 0:
                t2.next = None
            else:
                t2.next = stack.pop()
                t2.next.next = None

        return  head


if __name__ == '__main__':
    obj = ListNode(1)
    obj.next = ListNode(2)
    #obj.next.next = ListNode(3)
    #obj.next.next.next = ListNode(4)
    #obj.next.next.next.next = ListNode(5)
    #obj.next.next.next.next.next = ListNode(6)

    ob = Solution()
    head = ob.reorderList(obj)

    while head != None:
        print(head.val)
        head = head.next




