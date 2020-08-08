# link:  https://leetcode.com/problems/reverse-words-in-a-string-ii/


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # reverse the whole list
        self.reverse(s,0,len(s)-1)
        print(s)
        # reverse each single word
        left = 0
        for i in range(len(s)):
            if s[i] == " ":
                self.reverse(s,left,i-1)
                left=i+1
            if i==len(s)-1:
                self.reverse(s, left, i)

        
    def reverse(self, s,l,r):
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
                
        
