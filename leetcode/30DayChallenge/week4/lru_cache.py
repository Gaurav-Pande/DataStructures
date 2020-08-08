# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3309/
from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = OrderedDict()
        self.capacity = capacity

    def get(self, key):
    	"""
        :type key: int
        :rtype: int
        """
        if key in self.dic:
        	return -1
        value = self.dic.pop(key)
        self.dic[key] = value
        return value

    def put(self, key, value):
    	"""
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
        	self.dic.pop(key)
        else:
        	if len(self.dic)>=self.capacity:
        		self.dic.popitem(last=False)
        self.dic[key]=value


# doubly linked list implementation 
class Node:
def __init__(self, k, v):
    self.key = k
    self.val = v
    self.prev = None
    self.next = None

class LRUCache:
def __init__(self, capacity):
    self.capacity = capacity
    self.dic = dict()
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head

def get(self, key):
    if key in self.dic:
        n = self.dic[key]
        self._remove(n)
        self._add(n)
        return n.val
    return -1

def set(self, key, value):
    if key in self.dic:
        self._remove(self.dic[key])
    n = Node(key, value)
    self._add(n)
    self.dic[key] = n
    if len(self.dic) > self.capacity:
        n = self.head.next
        self._remove(n)
        del self.dic[n.key]

def _remove(self, node):
    p = node.prev
    n = node.next
    p.next = n
    n.prev = p

def _add(self, node):
    p = self.tail.prev
    p.next = node
    self.tail.prev = node
    node.prev = p
    node.next = self.tail

