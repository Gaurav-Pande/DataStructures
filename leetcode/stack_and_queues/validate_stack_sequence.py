# link: https://leetcode.com/problems/validate-stack-sequences/


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        
        stack = []
        j=0
        for num in pushed:
            stack.append(num)
            while stack and j<len(popped) and stack[-1]==popped[j]:
                stack.pop()
                j+=1
                
        if j==len(popped):
            return True
        else:
            return False