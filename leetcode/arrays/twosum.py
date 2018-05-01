#[https://leetcode.com/problems/two-sum/description/]

class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hash:
                return [nums_hash[target - nums[i]],i]
            else:
                nums_hash[nums[i]] = i
