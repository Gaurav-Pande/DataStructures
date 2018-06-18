# swap nodes in a link list
# link

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first_node = prev = ListNode(-1)
        prev.next = head

        if head != None and head.next != None:
            first = head
            second = head.next
            while first.next != None:
                first.next = second.next
                second.next = first
                prev.next = second
                if first.next == None or first.next.next == None:
                    break
                else:
                    prev = first
                    first = first.next
                    second = first.next


        return first_node.next



if __name__ == '__main__':
    obj = ListNode(1)
    obj.next = ListNode(2)
    obj.next.next = ListNode(3)
    #obj.next.next.next = ListNode(4)
    #obj.next.next.next.next = ListNode(5)
    #obj.next.next.next.next.next = ListNode(6)
    ob = Solution()
    head = ob.swapPairs(obj)
    while head:
        print (head.val)
        head = head.next







