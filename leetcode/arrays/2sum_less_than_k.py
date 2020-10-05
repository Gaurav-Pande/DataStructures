# link: https://leetcode.com/problems/two-sum-less-than-k/submissions/

class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # brute force method
        # using 2 pointer approach
        
        S = -1
        A.sort()
        l,r = 0, len(A)-1
        while l<r:
            if A[l] + A[r] <K:
                S = max(S, A[l]+A[r])
                l+=1
            else:
                r-=1
        return S
            
