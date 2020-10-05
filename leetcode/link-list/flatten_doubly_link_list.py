# link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        p = head
        
        while p:
        	# if there is no child then proceed to next node 
        	# until we dont find the child node
            if p.child == None:
                p=p.next
                continue
            # founc child node
            temp = p.child
            # now we find the tail of the child node branch
            while temp.next:
                temp = temp.next
            
            # find the tail of child node
            # conned it to the p node's next node 
            temp.next = p.next
            
            # connect p.next's previous to 
            # tail node 
            if p.next:
                p.next.prev = temp
            
            #  Connect p with p.child, and remove p.child
            p.next = p.child
            p.child.prev = p
            p.child = None
            
        return head
            
