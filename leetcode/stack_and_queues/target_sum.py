# https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/
class Solution(object):
    def __init__(self):
        self.cache = {}

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.calculateSum(nums, 0, 0, S)

    def calculateSum(self, nums, i, s, target):
        if (i, s) in self.cache:
            return self.cache[(i, s)]
        else:
            r = 0
            if i == len(nums):
                if s == target:
                    r = 1
            else:
                r = self.calculateSum(nums, i + 1, s - nums[i], target) + self.calculateSum(nums, i + 1, s + nums[i],
                                                                                            target)
            self.cache[(i, s)] = r
            return self.cache[(i, s)]
