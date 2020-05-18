#link:https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #########################################################
        ## Dp solution:
        ## similar to the maximum subarray
        ## find the difference between two consecutive days
        ## (only if there is a profit)
        ## and add all the profit
        ##########################################################
        dp = []
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                dp.append(prices[i]-prices[i-1])
        return sum(dp)