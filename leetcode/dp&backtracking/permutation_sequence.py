# link: https://leetcode.com/problems/permutation-sequence/
# explanation: https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1,n+1)]
        fact = []
        sum = 1
        fact.append(1)
        for i in range(1,n+1):
            sum *= i
            fact.append(sum)
        print(fact)
        # factorial[] = {1, 1, 2, 6, 24, ... n!}
        k-=1
        result = []
        for i in range(1,n+1):
            index = k/fact[n-i]
            result.append(nums[index])
            nums.pop(index)
            k = k-index*fact[n-i]
        print(result)   
        return "".join(result)