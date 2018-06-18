# sort a link list in O(nlogn)
# Link:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)

    def mergeSort(self,head):
        if head == None or head.next == None:
            return head

        head1, head2 = self.splitHalf(head)
        part1 = self.mergeSort(head1)
        part2 = self.mergeSort(head2)

        new_head = self.sortedMerge(part1, part2)

        return new_head

    def splitHalf(self, head):
        slow = head
        fast = head

        while fast != None and fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        second_head = slow.next
        slow.next = None

        return (head, second_head)

    def sortedMerge(self, head1, head2):
        dummy = head = ListNode(-1)

        while True:

            if head1 == None:
                dummy.next = head2
                break

            if head2 == None:
                dummy.next = head1
                break

            if head1.val <= head2.val:
                dummy.next = head1
                head1 = head1.next

            else:
                dummy.next = head2
                head2 = head2.next

            dummy = dummy.next

        return head.next

if __name__ == '__main__':
    obj = ListNode(1)
    obj.next = ListNode(3)
    obj.next.next = ListNode(2)
    obj.next.next.next = ListNode(6)
    obj.next.next.next.next = ListNode(5)
    obj.next.next.next.next.next = ListNode(0)

    ob = Solution()

    head = ob.sortList(obj)
    while head:
        print (head.val)
        head = head.next