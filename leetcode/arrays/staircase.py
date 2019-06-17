# https://leetcode.com/problems/climbing-stairs
class Solution(object):
    def __init__(self):
        self.dic = {}
    def climbStairs(self, n):
        return self.climb(0,n)
    def climb(self,i,n):
        if i in self.dic:
            return self.dic[i]
        else:
            if i == n:
                return  1
            if i > n:
                return 0
            self.dic[i+1] = self.climb(i+1,n)
            self.dic[i+2] = self.climb(i+2,n)
            return self.dic[i+1]+self.dic[i+2]

    # 100 percent faster, 4ms more optimized and fibonacci number
    def climbStairs1(self, n):
        if n in self.dic:
            return self.dic[n]
        if n in (0, 1):
            return 1
        else:
            self.dic[n] = self.climbStairs1(n - 2) + self.climbStairs1(n - 1)
            return self.dic[n]


if __name__ == "__main__":
    ob = Solution()
    print(ob.climbStairs1(10))


