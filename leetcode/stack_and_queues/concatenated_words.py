#link:  https://leetcode.com/problems/concatenated-words/

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # we can solve this using dfs solution
        
        allword = set(words)
        res = []
        for word in words:
            if self.dfs(word, allword):
                res.append(word)
        return res
    
    def dfs(self, word, allwords):
        for i in range(1,len(word)):
            prefix = word[:i]
            suffix = word[i:]
            
            if prefix in allwords and suffix in allwords:
                return True
            if prefix in allwords and self.dfs(suffix, allwords):
                return True
            if suffix in allwords and self.dfs(prefix, allwords):
                return True
        return False
