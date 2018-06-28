# Author: Gaurav Pande
# [Stacks: Balanced Brackets](https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem)

def is_matched(expression):
    stack1 = list(expression)
    stack2 = []
    opening_brackets = ["{","(","["]
    closing_brackets = ["}",")","]"]
    dict_sym = {"}":"{",")":"(","]":"["}
    while stack1:
        elem = stack1.pop(0)
        if elem in opening_brackets:
            stack2.append(elem)
        else:
            if stack2:
                if dict_sym[elem] == stack2[-1]:
                    stack2.pop()
                else:
                    return False
            else:
                return False
    
    if not stack1 and not stack2:
        return True
    else:
        return False
        
    
    
    

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")



# alternate and more pythonic solution

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if not stack or stack.pop() != dic[s[i]]:
                    return False
        return stack == []
