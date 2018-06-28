# Author: Gaurav Pande
# implement stack using queue
# link: https://leetcode.com/problems/implement-stack-using-queues/description/


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.top_element = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.top_element = x
        self.queue.append(x)

    def pop(self):
        """
        Removes the el
        :rtype: int
        """
        result = self.queue[-1]
        del self.queue[-1]
        if len(self.queue) != 0:
            self.top_element = self.queue[-1]
        return result

    def top(self):
        """
        Get the top element.
        :rtype: int
        """

        return self.top_element

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()