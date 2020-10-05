# link: https://leetcode.com/problems/word-break/


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # recursion
        # s = "leetcode", wordDict = ["leet", "code"]
        # recursion withour memoization will not pass
        #  in worst case 
        # s = "aaaaaaaaaa"
        return self.word_break(s , wordDict , 0)
    
    def word_break(self, s, wordDict, start):
        if start == len(s):
            return True
        for end in range(start+1,len(s)+1):
            # print(s[start:end])
            if s[start:end] in wordDict and self.word_break(s, wordDict, end):
                return True
            
        return False



# with memoization
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # recursion
        # s = "leetcode", wordDict = ["leet", "code"]
        
        return self.word_break(s , wordDict , 0, {})
    
    def word_break(self, s, wordDict, start, memo):
        if start == len(s):
            return True
        
        if start in memo:
            return memo[start]
        
        for end in range(start+1,len(s)+1):
            # print(s[start:end])
            if s[start:end] in wordDict and self.word_break(s, wordDict, end, memo):
                memo[start] = True
                return memo[start]
            
        memo[start]=False
        return memo[start]


# Dp soltion
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s)+1)]
        dp[0]= True
        
        for i in range(1,len(s)+1):
            for j in range(0,i):
                print(s[j:i])
                
                if dp[j] and s[j:i] in wordDict:
                    print("")
                    print(s[j:i])
                    
                    dp[i] = True
                    print(dp)
                    break