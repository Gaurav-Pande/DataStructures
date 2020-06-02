#link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        Keep on adding the sum to the list. [1,1,1,1], k=2
        sum would be = [0,1,2,3,4]
        at each index after calculating sum, check if sum-k is in the dictionary(this will hold the sum and its count)
        if sum-k is in there then there is a subarray we have found. in above example
        0-2=No, 1-2=No, 2-2=0(exist in the dictionary.. that means a subarray is found with sum 2=1,1)
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
