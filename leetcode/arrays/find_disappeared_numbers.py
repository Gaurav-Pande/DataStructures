# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i, v in enumerate(nums):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
            else:
                continue

        result = []
        for i, v in enumerate(nums):
            if v < 0:
                continue
            else:
                result.append(i + 1)

        return result