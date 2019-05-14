class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            j = i + k
            if j < len(nums):
                for a in range(i, j+1):
                    for b in range(a + 1, j+1):
                        r = (nums[a] - nums[b])
                        if abs(nums[a] - nums[b]) <= t:
                            return True
                        else:
                            continue
            else:
                for b in range(i + 1, len(nums)):
                    r = (nums[i] - nums[b])
                    if abs(nums[i] - nums[b]) <= t:
                        return True
                    else:
                        continue



        return False


if __name__ == '__main__':
    b = [2,2]
    k = 3
    t = 0
    a = Solution()
    print(a.containsNearbyAlmostDuplicate(b,k,t))