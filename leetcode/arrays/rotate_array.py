# https://leetcode.com/problems/rotate-array/
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:len(nums) - k] = self.reverse(nums[:len(nums) - k])
        nums[len(nums) - k:] = self.reverse(nums[len(nums) - k:])
        nums[:] = nums[::-1]

    def reverse(self, num):
        i = 0
        j = len(num) - 1
        while i < j:
            temp = num[j]
            num[j] = num[i]
            num[i] = temp
            i += 1
            j -= 1
        return num