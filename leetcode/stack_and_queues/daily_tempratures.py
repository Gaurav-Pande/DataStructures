#https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/

class Solution(object):
    # def __init__(self):
    #     self.cache = (0,0)
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(T)
        for index, elem in enumerate(T):
            while stack and T[stack[-1]] < elem:
                e = stack.pop()
                res[e] = index - e
            stack.append(index)
        return res

#         res = []
#         temp  = copy.deepcopy(T)
#         index  = 0
#         while T:
#             elem = T.pop(0)
#             count =  self.findmax(elem,index,temp)
#             res.append(count)
#             index += 1
#         return res

#     def findmax(self,elem, index,T):
#         if elem < self.cache[0]:
#             return self.cache[1] - index
#         result = index
#         for i in range(index,len(T)):
#             if elem < T[i]:
#                 break
#             else:
#                 result += 1
#         #print(index,result)
#         if result == len(T):
#             self.cache = (0,0)
#             return 0
#         else:
#             self.cache = (T[result],result)
#             return result-index

if __name__ == '__main__':
    ob = Solution()
    ob.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])

