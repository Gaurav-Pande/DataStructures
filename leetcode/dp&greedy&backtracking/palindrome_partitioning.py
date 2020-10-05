# link: https://leetcode.com/problems/palindrome-partitioning/
class Solution(object):
    def __init__(self):
        self.result = []
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.backTrack(0, len(s), [], s)
        return self.result
    
    def backTrack(self, start, end, temp, s):
        if start == end:
            self.result.append(temp[:]) 
        for i in range(start, end):
            curr = s[start:i+1]
            if curr == curr[::-1]:
                temp.append(curr)
                self.backTrack(i+1, end,  temp, s)
                temp.pop()
        return self.result
       
