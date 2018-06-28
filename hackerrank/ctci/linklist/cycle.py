# Author: Gaurav Pande
# [Linked Lists: Detect a Cycle](https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem)

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    temp1 = head
    temp2 = temp1
    if head == None or head.next == None:
        return False
    while temp1 != temp2 or temp1 != None:
        temp1 = temp1.next.next
        temp2 = temp2.next
        if temp1 == temp2:
            return True
        elif temp1 == None:
            return False
        
        
    
