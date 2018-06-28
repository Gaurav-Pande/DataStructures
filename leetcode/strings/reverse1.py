# Author: Gaurav Pande
# [344. Reverse String](https://leetcode.com/problems/reverse-string/description/)

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = len(s) - 1
        j = 0
        res = ""
        while i >= 0:
            res = res +  str(s[i])
            i = i - 1
            j = j + 1
        return res
