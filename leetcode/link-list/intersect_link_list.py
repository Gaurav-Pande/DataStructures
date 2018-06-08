# find the intersection point of 2 link list
# link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        tempA = headA
        countA = 1
        countB = 1
        tempB = headB

        if tempA == None or tempB == None:
            return None
        while tempA:
            tempA = tempA.next
            countA += 1
        while tempB:
            tempB = tempB.next
            countB += 1

        diff = countA - countB
        tempA = headA
        tempB = headB
        if diff < 0:
            diff = abs(diff)
            while diff != 0:
                tempB = tempB.next
                diff -= 1
        else:
            while diff != 0:
                tempA = tempA.next
                diff -= 1
        while tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next

            if tempA == None or tempB == None:
                return None

        return tempA


    def getIntersectionNode_better_approach(self,headA,headB):
        """
               :type head1, head1: ListNode
               :rtype: ListNode

        """
        
        tempa = headA
        tempb = headB

        if tempa == None or tempb == None:
            return None

        while tempa != tempb:
            if tempa != None and tempb != None:
                tempa = tempa.next
                tempb = tempb.next
            elif tempa == None:
                tempa = headB
            else:
                tempb = headA

        return tempa if tempa != None else None


