# Author: Gaurav Pande
# check whether a string is a balanced paranthesis or not
# link: https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack1 = list(s)
        stack2 = []
        open_brac = ["{", "(", "["]
        close_brac = ["}", ")", "]"]
        dict_sym = {"}": "{", ")": "(", "]": "["}

        while stack1:
            elem = stack1.pop(0)
            if elem in open_brac:
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


# alternate and more pythonic solution

class Solution2(object):
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
