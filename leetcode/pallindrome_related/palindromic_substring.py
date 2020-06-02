#link: https://leetcode.com/problems/palindromic-substrings/
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res = self.helper(i,i,s,res)
            res = self.helper(i,i+1,s,res)
        return res
    
    def helper(self,left,right,s,res):
        while left>=0 and right<len(s) and s[left]==s[right]:
            res+=1
            left-=1
            right+=1
        return res
            
            
            