# link: https://leetcode.com/problems/two-city-scheduling/


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # sort by the difference in first and second value
        # which indicated the extra cost involve in sending a person to 
        # to A or B
        
        sorted_list = sorted(costs, key = lambda a: a[0]-a[1])
        # print(sorted_list)
        n = len(costs)//2
        result = 0
        for i in range(n):
            result += sorted_list[i][0] + sorted_list[i+n][1]
            
        return result
        
