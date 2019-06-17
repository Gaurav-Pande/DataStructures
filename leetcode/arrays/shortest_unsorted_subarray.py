#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The below solution is the naive solution it generally going to take O(Nlogn + N) time complexity to do
        # n = sorted(nums)
        # print(n)
        # count = 0
        # i = 0
        # j = 0
        # t_list = []
        # while i < len(nums) and j < len(n):
        #     if nums[i] != n[j]:
        #         t_list.append((i, nums[i]))
        #     i += 1
        #     j += 1
        #
        # if not t_list:
        #     return 0
        # else:
        #     count = t_list[-1][0] - t_list[0][0] + 1
        # return count

        # Better solution here O(N):
        i = 0
        j = -1
        l = 0
        r = len(nums) - 1
        import sys
        mn = sys.maxsize
        mx = -sys.maxsize - 1
        while l < len(nums) and r >= 0:
            mx = max(mx, nums[l])
            if nums[l] != mx:
                j = l
            mn = min(mn, nums[r])
            if nums[r] != mn:
                i = r
            l += 1
            r -= 1

        return (j - i + 1)