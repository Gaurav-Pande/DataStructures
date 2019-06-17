# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        # TME solution
        # i, j = 0, 1
        # while j<len(S):
        #     if S[i] == S[j]:
        #         S = S[:i] + S[j+1:]
        #         i=-1
        #         j=0
        #     i += 1
        #     j += 1

        res = []
        i = 0
        for elem in S:
            if res and res[-1] == elem:
                res.pop()
            else:
                res.append(elem)

        return "".join(res)


