# link: https://leetcode.com/problems/find-k-closest-elements/
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l,r = 0, len(arr)-k
        while l<r:
            mid = (l+r)//2
            if x-arr[mid] > arr[mid+k]-x:
                l +=1
            else:
                r-=1
                
        return arr[l:l+k]
        
        
            
            
                
            
