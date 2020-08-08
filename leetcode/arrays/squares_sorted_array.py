# link: https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return self.mergeSort([x**2 for x in A])
    
    
    def mergeSort(self,nums):
        if len(nums)<2:
            return nums[:]
        else:
            mid = (len(nums))//2
            left = self.mergeSort(nums[:mid])
            right = self.mergeSort(nums[mid:])
            # print(left,right)
            return self.merge(left,right)

        
        
    def merge(self,left, right):
        i,j=0,0
        res = []
        # print(left,right)
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        while i<len(left):
            res.append(left[i])
            i+=1
            
        while j<len(right):
            res.append(right[j])
            j+=1
        return res
