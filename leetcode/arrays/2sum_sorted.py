# link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dic:
                return [dic[target-numbers[i]], i+1]
            else:
                dic[numbers[i]]=i+1



# two pointer method

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pointer method
        l,r = 0, len(numbers)-1
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r] > target:
                r -= 1
            else:
                l +=1
        
        
            
        