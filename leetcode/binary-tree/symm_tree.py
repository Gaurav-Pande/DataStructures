# Author: Gaurav Pande
# find whether a tree is symmetric or not by itself
# link: https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# Final Solution
# Using Recursion
#


class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        else:
            return self.check(root.left, root.right)

    def check(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        return p.val == q.val and self.check(p.right, q.left) and self.check(p.left, q.right)





#
#
# Iterative Solution without recursion
#
#
class SolutionBfs:
    def isSymmetric(self, root):
        q = collections.deque()
        if root == None:
            return True
        else:
            q.append((root, root))
            while q:
                first, second = q.popleft()
                if first == None and second == None:
                    continue
                if first == None or second == None:
                    return False
                if first.val == second.val:
                    q.append((first.left, second.right))
                    q.append((first.right, second.left))
                else:
                    return False
        return True









        ## Wrong solution, can not use bfs here because:
## lost 3 hours in it !!!
##it fails in [2,3,3,4,5,5,4,null,null,8,9,null,null,9,8]
import collections

class Solution2:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l = self.levelOrder(root)
        print(l)
        result = False
        if l == []:
            return False

        for k,v in l.items():
            if k == 0:
                continue
            else:
                result = self.isPalindrome(v)

        return result



    def isPalindrome(self,l):
        print(l)
        res = False

        if len(l)%2 != 0:
            return False
        else:
            while len(l) >= 2:
                elem1,pos1 = l.pop(0)
                elem2,pos2 = l.pop()
                print(elem1,elem2)
                if elem1 == elem2 and pos1 != pos2:
                    res = True
                else:
                    res = False
                    break

        return res




    def levelOrder(self, root):
        result = collections.defaultdict(list)
        q = collections.deque()
        level = 0
        if root == None:
            return []
        else:
            q.append((root, level, "root"))
            while q:
                elem, level, pos = q.popleft()
                result[level].append((elem.val,pos))
                if elem.left:
                    q.append((elem.left,level+1,"left"))
                if elem.right:
                    q.append((elem.right,level+1, "right"))

        return result


if __name__  == '__main__':
    obj = TreeNode(1)
    obj.left = TreeNode(2)
    obj.right = TreeNode(2)
    obj.left.left = TreeNode(3)
    obj.left.right = TreeNode(4)
    obj.right.right = TreeNode(3)

    ob = Solution()
    print(ob.isSymmetric(obj))