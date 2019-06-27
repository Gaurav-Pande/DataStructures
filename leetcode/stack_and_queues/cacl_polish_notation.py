# https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i, v in enumerate(tokens):
            stack.append(v)
            while len(stack) != 1 and stack[-1] in ['+', '-', '*', '/']:
                oper = stack.pop()
                elem1 = stack.pop()
                elem2 = stack.pop()
                stack.append(self.operate(elem1, elem2, oper))

        return stack[0]

    def operate(self, elem1, elem2, oper):
        print(elem1, elem2, oper)
        if oper == '+':
            return int(elem2) + int(elem1)
        elif oper == '*':
            return int(elem2) * int(elem1)
        elif oper == '-':
            return int(elem2) - int(elem1)
        else:
            return (
                int(elem2) // int(elem1) + 1 if int(elem1) * int(elem2) < 0 and int(elem2) % int(elem1) != 0 else int(
                    elem2) // int(elem1))
