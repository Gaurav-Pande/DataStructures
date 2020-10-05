#link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum = 0
        minprice = float('inf')
        print(zip(prices,prices[1:]))
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            maximum = max(maximum, prices[i]-minprice)
                
            
            
            
        return maximum
            
