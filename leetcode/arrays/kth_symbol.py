# https://leetcode.com/problems/k-th-symbol-in-grammar
class Solution:
    def kthGrammar(self, N, K):
        if N == 1:
            return 0
        half = 2 ** (N - 2)
        if K <= half:
            return self.kthGrammar(N - 1, K)
        else:
            res = self.kthGrammar(N - 1, K - half)
            if res == 0:
                return 1
            else:
                return 0
