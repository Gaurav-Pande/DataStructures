# [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/description/)

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        list_s = s.split(" ")
        ob = Solution()
        for item in list_s:
            res = res + " " + ob.reverseString(item)
        return res.lstrip()
            
            
    def reverseString(self,s):
        i = len(s) - 1
        j = 0
        res = ""
        for elem in s:
            res = res + str(s[i])
            i = i - 1
            j = j + 1
        return res
