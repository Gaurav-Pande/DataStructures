class Solution:
    def decodeString(self, s):
        # steps
        # start pushing the elems in the stack 1 by 1
        # once we encounter "]" we start popping out until we saw a number
        # we retrieve the string
        # start pushing
        stack = []
        t = []
        if not s:
            return ""
        cs = ""
        cn = 0
        for elem in s:
            if elem == '[':
                stack.append(cs)
                stack.append(cn)
                cs = ""
                cn = 0
            elif elem == ']':
                num = stack.pop()
                ts = stack.pop()
                cs = ts + int(num) * cs
            elif elem.isdigit():
                cn = 10 * cn + int(elem)
            else:
                cs += elem

        return cs


if __name__ == '__main__':
    ob = Solution()
    print(ob.decodeString("3[a]2[bc]"))