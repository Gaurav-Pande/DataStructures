# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
# split a array into 3 equal subarray

def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s= sum(A)
        if s%3!=0:
            return False
        each_sum = s/3
        result = [2*each_sum,each_sum]
        temp =0
        for val in A:
            if not result:
                return True
            else:
                temp += val
                if temp == result[-1]:
                    result.pop()
        return False