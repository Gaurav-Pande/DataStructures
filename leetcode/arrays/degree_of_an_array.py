# link: https://leetcode.com/problems/degree-of-an-array/

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        sorted_c = sorted(c.items(), key=lambda k:k[1], reverse=True)
        degree = sorted_c[0][1]
        if degree == 1:
            return 1
        res = 50000
        # print(degree)
        # print(sorted_c)
        for k,v in sorted_c:
            if v == degree:
                res = min(res,self.findSub(nums,k))
    
        return res
    def findSub(self, nums, num):
        indexes= []
        for i in range(len(nums)):
            if nums[i]==num:
                indexes.append(i)
        # print(indexes)
        return indexes[-1]-indexes[0]+1
        
