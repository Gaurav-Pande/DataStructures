# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3292/


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