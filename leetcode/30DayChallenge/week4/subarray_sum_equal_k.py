#link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        dic = {}
        dic[0] = 1
        c_sum = 0
        result =0
        for i in range(len(nums)):
            c_sum += nums[i]
            if c_sum-k in dic:
                result += dic[c_sum-k]
            if c_sum in dic:
                dic[c_sum] += 1
            else:
                dic[c_sum] = 1
                
        return result
