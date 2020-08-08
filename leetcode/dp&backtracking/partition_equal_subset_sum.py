# link: https://leetcode.com/problems/partition-equal-subset-sum/
# solution explanation:  https://leetcode.com/problems/partition-equal-subset-sum/discuss/462699/Whiteboard-Editorial.-All-Approaches-explained.


class Solution(object):
    def __init__(self):
        self.st = {}
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums = sorted(nums, reverse=True)
        s = sum(nums)
        if s%2 != 0:
            return False
        print(nums)
        
        target = s//2
        print(target)
        
        return self.backtracking(nums, target)
    
    def backtracking(self, nums, curr):
        if curr<0:
            return False
        if curr == 0:
            return True
        for i in range(len(nums)):
        	# for TLE check if the current number is greater than the remaining sum
            if nums[i] > curr:
                return False
            return self.backtracking(nums[i+1:], curr-nums[i]) or self.backtracking(nums[i+1:],curr)
        return False
             
        
