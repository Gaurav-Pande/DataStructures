# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ######
        ## The idea is to store the unique elements in a set
        ## then loop over the original array and check if its plus exist in set
        ## if yes then result+1
        ## remember each duplicate element is treated differently here
        ##
        ##
        count = 0
        s= set(arr)
        for num in arr:
            if num+1 in s:
                count+=1
        return count