# link: https://leetcode.com/problems/merge-intervals/submissions/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        sorted_in = sorted(intervals, key =lambda k: k[0])
        # print(sorted_in)
        for num in sorted_in:
            f,s = num[0],num[1]
            if not result or result[-1][1]<f:
                result.append(num)
            else:
                l = result[-1][1]
                if l>=f:
                    result[-1][1] = max(result[-1][1],s)
        return result