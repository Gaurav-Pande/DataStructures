# copy  a linked list which contains a random pointer with it
# link: https://leetcode.com/problems/copy-list-with-random-pointer/description/

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def copyRandomList(self, head):
    dic = dict()
    m = n = head
    # first create  dictionary and clone each and every element
    while m:
        dic[m] = RandomListNode(m.label)
        m = m.next
    # again parse the link list
    # now here we copy the links
    while n:
        dic[n].next = dic.get(n.next)
        dic[n].random = dic.get(n.random)
        n = n.next
    return dic.get(head)