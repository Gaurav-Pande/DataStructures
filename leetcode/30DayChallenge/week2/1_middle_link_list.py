# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3290/


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        second = head
        while second.next and second:
            print(second.val)
            first = first.next
            if not second.next.next:
                break
            else:
                second = second.next.next
        return first