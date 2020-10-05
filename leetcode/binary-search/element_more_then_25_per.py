# link:  https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

# linear time solution
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # clever solution
        l = len(arr)//4
        for i in range(len(arr)):
            if arr[i] == arr[i+l]:
                return arr[i]