#  https://leetcode.com/problems/contains-duplicate-iii/submissions/
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Time limit Exceeded solution
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


# Bucket Solution
# Maintain buckets each of size t+1 holding the last k elements. This is the invariant.
# Buckets are [0, t], [t+1,2t+1], [2t+2, 3t+2],....
# What are the conditions of a match? Either x lies in a bucket which already has a member (this directly means that x and this element are within t of each other). Or the two neighbors of around this bucket may have a potential match. Check the code for an explanation.
# Lastly we notice how we purge elements from the cache/buckets which are stale i.e. outside the window of k elements.
# Notice one more thing: -3//5 = -1 - Python does this automatically and hence we dont need any special magic for handling negative numbers.
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        buckets = {}
        for i in range(len(nums)):
            if i > k:
                bucket_to_delete = nums[i - k - 1] // (t + 1)
                del buckets[bucket_to_delete]
            bucket = nums[i] // (t + 1)
            if bucket in buckets:
                return True
            for b in (bucket - 1, bucket + 1):
                if b in buckets and abs(buckets[b] - nums[i]) <= t:
                    return True
            buckets[bucket] = nums[i]
        return False


if __name__ == '__main__':
    b = [2,2]
    k = 3
    t = 0
    a = Solution()
    print(a.containsNearbyAlmostDuplicate(b,k,t))