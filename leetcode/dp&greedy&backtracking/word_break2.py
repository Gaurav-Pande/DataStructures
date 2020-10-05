# link: https://leetcode.com/problems/word-break-ii/

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.backtrack(s,0, wordDict, {})

    
    def backtrack(self, s, start, wordDict, memo):
    	# starting with index start
    	# how many words we can find out
        print(s, start, memo)
        if start in memo:
            return memo[start]
        else:
            res = []
            for word in wordDict:
                if start + len(word) == len(s)  and s[start:start+len(word)] == word:
                    # search end here and we add the resu
                    res.append(word)
                if start + len(word) < len(s) and s[start:start+len(word)] == word:
                    suffix_result = self.backtrack(s, start+len(word),wordDict, memo )
                    print(suffix_result)
                    for sub in suffix_result:
                        res.append(word + " " + sub)
            memo[start] = res
            return res
                    
        
        
        
            
        
         
        
    
            
