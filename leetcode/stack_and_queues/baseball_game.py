#link: https://leetcode.com/problems/baseball-game/


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # ["5","2","C","D","+"]
        # 5, 2(7), 0(5), 10(15), 15(30)
        
        if not ops:
            return None
        
        stack = []
        
        for o in ops:
            if o == '+':
                stack.append(stack[-1] + stack[-2])
            elif o == 'C':
                stack.pop()
            elif o == 'D':
                stack.append(2*stack[-1])
            else:
                stack.append(int(o))
                
        return sum(stack)
                
            
