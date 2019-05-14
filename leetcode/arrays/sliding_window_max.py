# We scan the array from 0 to n-1, keep "promising" elements in the deque. The algorithm is amortized O(n) as each element is put and polled once.
#
# At each i, we keep "promising" elements, which are potentially max number in window [i-(k-1),i] or any subsequent window. This means
#
# If an element in the deque and it is out of i-(k-1), we discard them. We just need to poll from the head, as we are using a deque and elements are ordered as the sequence in the array
#
# Now only those elements within [i-(k-1),i] are in the deque. We then discard elements smaller than a[i] from the tail. This is because if a[x] <a[i] and x<i, then a[x] has no chance to be the "max" in [i-(k-1),i], or any other subsequent window: a[i] would always be a better candidate.
#
# As a result elements in the deque are ordered in both sequence in array and their value. At each step the head of the deque is the max element in [i-(k-1),i]
# https://leetcode.com/problems/sliding-window-maximum/

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # TLE solution below
        # i=0
        # result = []
        # max_elem = - sys.maxint -1
        # win = k
        # while i<len(nums):
        #     r = i
        #     while r <= k-1 and k <=len(nums):
        #         #print(max_elem,nums[r])
        #         max_elem = max(max_elem,nums[r])
        #         r +=1
        #     if max_elem != -sys.maxint -1:
        #         result.append(max_elem)
        #     max_elem = - sys.maxint -1
        #     i+= 1
        #     k+=1
        # return result

        # one pass
        if not nums:
            return []

        if k == 2:
            return nums
        i = 0
        import collections
        d = collections.deque()
        result = []
        while i < k:
            while d:
                if nums[i] > nums[d[-1]]:
                    d.pop()
                else:
                    break
            d.append(i)
            i += 1

        print(d)
        j = k
        while j < len(nums):
            result.append(nums[d[0]])
            if d[0] < j - k + 1:
                d.popleft()
            while d:
                if nums[j] > nums[d[-1]]:
                    d.pop()
                else:
                    break
            d.append(j)
            print(d)
            j += 1

        result.append(nums[d[0]])

        return result



