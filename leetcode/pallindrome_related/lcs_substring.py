# https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
		result  = ""
		for i in range(len(s)):
			temp  = self.helper(s,i,i)
			if len(temp)> len(result):
				result = temp
			temp = self.helper(s,i,i+1)
			if len(result)<len(temp):
				result = temp
		return result

def helper(self,s,l,r):
	while l>=0 and r<len(s) and s[l]==s[r]:
		l-=1
		r+=1
	return s[l+1:r]



