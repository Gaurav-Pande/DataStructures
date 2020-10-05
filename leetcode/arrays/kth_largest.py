#link: https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)
                
        return heap[-k]