# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        res = []
        # [ -4,-1,,-1, 0, 1, 2]
        nums = sorted(nums)

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                print(nums)
                print(nums[i], nums[l], nums[r])
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res

