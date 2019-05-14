# https://leetcode.com/problems/next-greater-node-in-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        result = []
        stack = []

        while head:
            while stack and stack[-1][1] < head.val:
                top = stack.pop()[0]
                result[top] = head.val
            stack.append([len(result), head.val])
            result.append(0)
            head = head.next
        # print result
        return result
        # Bruteforce approach
#         a = head
#         b = head
#         result = []
#         count  = 0
#         while a:
#             b = b.next
#             count += 1

#             #print("her",temp1.val)
#             if b == None and a != None:
#                 #print("here",temp1.val)
#                 result.append(0)
#                 a = a.next
#                 b = a
#             if a != None and b != None and  a.val < b.val:
#                 print(a.val,b.val)
#                 result.append(b.val)
#                 a = a.next
#                 b = a

#         print(result)
#         return result

