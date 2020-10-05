#link: https://leetcode.com/problems/minimum-cost-to-merge-stones/

class Solution(object):
    def mergeStones(self, stones, K):
        def recursive(i, j, piles):
            if i == j and piles == 1:
                return 0
            if (j - i + 1 - piles) % (K - 1) != 0: 
                return float('inf')  # means impossible
            if (i, j, piles) in dp:
                return dp[(i, j, piles)]
            if piles == 1:
                dp[(i,j,piles)] = recursive(i, j, K) + pre_sum[j+1] - pre_sum[i]
                return dp[(i,j,piles)]
            else:
                min_cost = float('inf')
                for k in range(i, j, K - 1):
                    min_cost = min(min_cost, recursive(i, k, 1) + recursive(k + 1, j, piles - 1))
                dp[(i, j, piles)] = min_cost
                return dp[(i, j, piles)]
        
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + stones[i]
        dp = {}
        return recursive(0, n - 1, 1)