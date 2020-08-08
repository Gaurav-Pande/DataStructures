#link:https://leetcode.com/problems/subsets

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sorting is done  so that duplicate elements are always handled at last
        nums =  sorted(nums)
        res = []
        self.backtrack(nums, 0, res, [] )
        return res
        
    def backtrack(self, nums, index, res, temp):
        res.append(temp[:])
        for i in range(index, len(nums)):
            # add the current number to the comb
            self.backtrack(nums, i+1, res, temp+[nums[i]])
    
