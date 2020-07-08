# link: https://leetcode.com/problems/interleaving-string/solution/
# hard question

# Recursion
class Solution(object):
    def __init__(self):
        self.dic = {}
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        return self.isInter(s1,0,s2,0,"",s3)

    
    def isInter(self, s1, i, s2, j, res, s3):
        print(i,j, res)
        if res == s3 and i==len(s1) and j==len(s2):
            return True
        ans = False
        if i < len(s1):
            ans = ans or self.isInter(s1, i+1, s2, j, res + s1[i],s3 )

        if j < len(s2):
            ans = ans or self.isInter(s1, i, s2, j+1, res +s2[j], s3)
              
            
        return ans


# Recursion with memoization

class Solution(object):
    def __init__(self):
        self.dic = {}
    def isInterleave(self, s1, s2, s3, memo={}):
        if len(s1) + len(s2) != len(s3): return False
        if not s1 and not s2 and not s3: return True
        if (s1, s2, s3) in memo:         return memo[s1, s2, s3]
        memo[s1,s2,s3] =\
               (len(s1) > 0 and len(s3) > 0 and s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:], memo)) or\
               (len(s2) > 0 and len(s3) > 0 and s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:], memo))
        return memo[s1,s2,s3]


# DP solution
 class Solution(object):
    def isInterleave(self, s1, s2, s3, memo={}):
        if len(s1) + len(s2) != len(s3): 
            return False
        dp = [[False]*(len(s2)+1) for i in range(len(s1)+1)]
        # print(dp)
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if (i==0 and j==0):
                    dp[i][j] = True
                elif i ==0:
                    dp[i][j] = dp[i][j-1] and s2[j-1]==s3[i+j-1]
                elif j==0:
                    dp[i][j] = dp[i-1][j] and s1[i-1]==s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[len(s1)][len(s2)]
