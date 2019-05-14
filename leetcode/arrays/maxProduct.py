# https://leetcode.com/problems/maximum-product-of-three-numbers/


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method 1: Soring
        # l = sorted(nums)
        # return max(l[0]*l[1]*l[-1],l[-1]*l[-2]*l[-3])

        # method 2: Single scan

        min1 = min2 = sys.maxint
        max1 = max2 = max3 = -sys.maxint - 1
        for elem in nums:
            if elem <= min1:
                min2 = min1
                min1 = elem
            elif elem < min2:
                min2 = elem
            if elem >= max1:
                max3 = max2
                max2 = max1
                max1 = elem
            elif elem >= max2:
                max3 = max2
                max2 = elem
            elif elem > max3:
                max3 = elem

        return max(min1 * min2 * max1, max1 * max2 * max3)
