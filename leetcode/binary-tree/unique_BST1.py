# https://leetcode.com/problems/unique-binary-search-trees/submissions/
class Solution:
    def __init__(self):
        self.dic = {}

    def numTrees(self, n: int) -> int:
        # notice here that we have used the floor integer division because using // we can divide as many
        # large number as we can.
        # for reference look here: https://stackoverflow.com/questions/27946595/how-to-manage-division-of-huge-numbers-in-python
        return self.fact(2 * n) // (self.fact(n) * self.fact(n + 1))

    # using DP, storing intermediate resul in a dictionary and use the for loop twice to calculate the
    # the catalan number
    # def catalin(self,n:int) -> int:
    #     dic = {}
    #     dic[0]=dic[1] =1
    #     result = 1
    #     i = 2
    #     while i<=n:
    #         j=0
    #         dic[i] = 0
    #         while j<i:
    #             dic[i] = dic[i] + dic[j]*dic[i-j-1]
    #             #print(dic[i],i)
    #             j+=1
    #         i+=1
    #     return dic[n]

    # using factorial or DP combine
    def fact(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        else:
            if n in self.dic:
                return self.dic[n]
            else:
                self.dic[n] = (n) * self.fact(n - 1)
                return self.dic[n]

















