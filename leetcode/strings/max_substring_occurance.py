#link: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        
        k = minSize
        l = []
        for i in range(len(s)-k+1):
            l.append(s[i:i+k])
        count  = collections.Counter(l)
        res  = 0
        for w,f in count.items():
            if len(set(w)) <= maxLetters:
                res = max(res, f)
        return res
            
            
                
            
        
                
                
            
            
        
