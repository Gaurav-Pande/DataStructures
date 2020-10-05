# link: https://leetcode.com/problems/3sum-smaller/submissions/

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float('inf')
        nums.sort()
        result = 0
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while l<r:
                c = nums[i] + nums[l] + nums[r]
                if c < target:
                    # print(nums[i], nums[l], nums[r])
                    result += (r-l)
                    l+=1
                else:
                    r-=1
            
        return result
                
                    