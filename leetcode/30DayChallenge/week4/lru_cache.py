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
