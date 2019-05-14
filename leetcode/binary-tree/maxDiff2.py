# https://leetcode.com/contest/weekly-contest-132/problems/maximum-difference-between-node-and-ancestor/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.max = 0
        self.min = 10000

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return  self.findMaxDiff(root ,10000 ,0)

    def iq_test(self,numbers):
        # your code here
        even = []
        odd = []
        numbers = list(numbers.split(" "))
        for i in range(0,len(numbers)):
            if numbers[i] % 2 == 0:
                even.append((i + 1, numbers[i]))
            else:
                odd.append((i + 1, numbers[i]))
        if len(even) == 1:
            return even[0][0]
        else:
            return odd[0][0]

    def findMaxDiff(self ,root ,mn ,mx):
        if not root:
            return mx -mn
        mx = max(mx ,root.val)
        mn = min(mn ,root.val)
        print(mx ,mn)
        a = self.findMaxDiff(root.left ,mn ,mx)
        b = self.findMaxDiff(root.right ,mn ,mx)
        print(a ,b ,max(a ,b))
        return max(a ,b)



    # def findMaxDiff(self,root):
    #     if not root:
    #         return 10000
    #     if not root.left and not root.right:
    #         return root.val
    #     val = min(self.findMaxDiff(root.left),self.findMaxDiff(root.right))
    #     print(val)
    #     diff = abs(root.val-val)
    #     self.max = max(self.max, diff)
    #     print(self.max)
    #     return min(root.val,val)










