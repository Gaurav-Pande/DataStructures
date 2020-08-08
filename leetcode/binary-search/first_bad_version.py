#link: https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n
        f =1
        while l<=r:
            mid = (l+r)//2
            if isBadVersion(mid):
                f = mid
                if mid == 0 or not isBadVersion(mid-1):
                    break
                else:
                    r = mid-1
            else:
                l = mid+1
        return f
                
