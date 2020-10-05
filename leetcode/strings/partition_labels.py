# link: https://leetcode.com/problems/partition-labels/

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        start = 0
        length = 0
        dic = {c:i for i,c in enumerate(S)}
        result = []
        for i in range(len(S)):
            start = max(start,dic[S[i]])
            if i==start:
                result.append(i-length+1)
                length = i+1
        return result
        
