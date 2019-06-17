# https://leetcode.com/problems/remove-outermost-parentheses/submissions/
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        "(()())(())(()(()))"
        """
        # Method 1 using stack
        stack = []
        res = ""
        s = []
        for elem in S:
            if elem == "(":
                res = res + elem
                stack.append(elem)

            if elem == ")":
                spop = stack.pop()
                if not stack:
                    res = res[1:]
                    s.append(res)
                    res = ""
                else:
                    res = res + elem

        # print(s)
        return "".join(s)

        # Method 2
#         counter  = 0
#         result = []
#         current_paran = []
#         for i in range(len(S)):
#             current_paran.append(S[i])
#             if S[i] == "(":
#                 counter += 1
#             else:
#                 counter -= 1

#             if counter == 0:
#                 result.append("".join(current_paran[1:-1]))
#                 current_paran = []

#         return "".join(result)








