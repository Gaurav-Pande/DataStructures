# link: https://leetcode.com/problems/minimum-cost-to-connect-sticks/


class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heap = []
        for stick in sticks:
            heapq.heappush(heap, stick)
            
        # we pick minimum lenght stick and keep on adding until we are done
        total_cost = 0
        while len(heap)!=1:
            stick1 = heapq.heappop(heap)
            if heap:
                stick2 = heapq.heappop(heap)
            else:
                stick2 = 0
            total_cost += stick1+stick2
            heapq.heappush(heap,(stick1+stick2))
            
        return total_cost
