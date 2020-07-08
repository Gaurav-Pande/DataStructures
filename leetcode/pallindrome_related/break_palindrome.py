#link: https://leetcode.com/problems/break-a-palindrome/
class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        for i in range(len(palindrome)/2):
            if palindrome[i] != 'a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        if len(palindrome)==1:
            return ""
        else:
            return palindrome[:-1]+'b'