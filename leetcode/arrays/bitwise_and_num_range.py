#link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3308/

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        s = 0
        while m<n:
            m=m>>1
            n=n>>1
            s +=1
        return m<<s
        