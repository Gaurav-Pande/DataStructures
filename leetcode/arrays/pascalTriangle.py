# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/1659/

class Solution(object):
    def __init__(self):
        self.dic = {}

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        i = 1
        result = []

        while i <= numRows:
            temp = []
            j = 1
            while j <= i:
                if (i, j) in self.dic:
                    temp.append(self.dic[(i, j)])
                else:
                    self.dic[(i, j)] = self.findNumber(i, j)
                    temp.append(self.dic[(i, j)])
                j += 1
            result.append(temp)
            i += 1
        return result

    def findNumber(self, i, j):
        if (i, j) in self.dic:
            return self.dic[(i, j)]
        else:
            if j == 1 or j == i:
                # self.result.append([1])
                return 1
            a = self.findNumber(i - 1, j - 1)
            b = self.findNumber(i - 1, j)
            self.dic[(i, j)] = a + b
            return a + b




