# add to numbers without reversing the link list
# link:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = self.findlength(l1)
        len2 = self.findlength(l2)
        if len1 > len2:
            head2 = self.addleadingzeros(l2, len1 - len2)
            c, new_head = self.addlist(l1, head2)
        elif len1 < len2:
            head1 = self.addleadingzeros(l1, len2 - len1)
            c, new_head = self.addlist(head1, l2)
        else:
            c, new_head = self.addlist(l1, l2)

        if c > 0:
            node = ListNode(c)
            node.next = new_head
            new_head = node

        return new_head

    def findlength(self, head):
        if head == None:
            return 0
        count = 0
        while head != None:
            count += 1
            head = head.next
        return count

    def addleadingzeros(self, head, num):
        while num > 0:
            node = ListNode(0)
            node.next = head
            head = node
            num -= 1
        return head
    # recursive 
    def addlist(self, head1, head2):
        if head1==None and head2==None:
            return (0, None)
        c,p = self.addlist(head1.next, head2.next)
        s = head1.val + head2.val + c
        c = int(s / 10)
        ans = ListNode(s%10)
        ans.next = p
        return (c, ans)


if __name__ == '__main__':
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next =ListNode(6)
    l2.next.next = ListNode(4)
    ob = Solution()
    head = ob.addTwoNumbers(l1,l2)
    while head:
        print (head.val)
        head = head.next



