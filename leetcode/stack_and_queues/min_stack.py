# Author: Gaurav Pande
# implement stack in python with an additional feature of getMIN
# link: https://leetcode.com/problems/min-stack/description/

import sys
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        current_min = self.getMin()
        if x < current_min or current_min == None:
            current_min = x
        self.stack.append((x, current_min))

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            result, minimum = self.stack[-1]
            return result

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            top, result = self.stack[-1]
        return result


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()





## This is my time limit exceeded solution
## as in getmin method i am traversing the whole list to get the minimun
class MinStackrejected(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = +sys.maxsize

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack)):
            if self.stack[i] < self.min:
                self.min = self.stack[i]
            else:
                continue
        result = self.min
        self.min = sys.maxsize
        return result

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()