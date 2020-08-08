# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # we traverse the list ot know which element is which
        # since the array is sorted then element at i must be greater then elem at i-2
        # so if i < 2 
        i=0
        for num in nums:
            if i<2 or num>nums[i-2]:
                nums[i] = num
                i+=1
        return i


 class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        j = 1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count += 1
            else:
                count = 1
            
            # now if the number of duplicates are 2 then we
            if count<=2:
                nums[j]=nums[i]
                j+=1
        return j