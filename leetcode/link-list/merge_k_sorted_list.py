#link: https://leetcode.com/problems/merge-k-sorted-lists/submissions/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = temp = ListNode(0)
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
                
        while heap:
            val, node = heapq.heappop(heap)
            temp.next = ListNode(val)
            temp = temp.next
            node = node.next
            if node:
                heapq.heappush(heap,(node.val, node))
                
        return head.next
            
        