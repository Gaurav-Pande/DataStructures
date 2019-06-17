# https://leetcode.com/problems/ugly-number-ii/
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        u = [1]
        i, j, k = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * u[i], 3 * u[j], 5 * u[k]
            m = min(u2, u3, u5)
            # print(m)
            if m == u2:
                i += 1
            if m == u3:
                j += 1
            if m == u5:
                k += 1
            u.append(m)
            n -= 1
        return u[-1]
