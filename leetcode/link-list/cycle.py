# Author: Gaurav Pande
# Detect the cycle in a link list
# link: https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return True

    def hasCycleHash(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        table = {}
        while head != None:
            if head in table.keys():
                return True
            else:
                table[head] = head.val
                head = head.next
                print(table)
        return False


if __name__ == '__main__':
    obj = ListNode(1)
    obj.next = obj
    a = Solution()
    print(a.hasCycleHash(obj))


