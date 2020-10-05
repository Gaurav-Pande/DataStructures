#link:  https://leetcode.com/problems/k-closest-points-to-origin
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # using normal sorting
        points = sorted(points, key = lambda k: k[0]**2 + k[1]**2)
        return points[:K]

# using heap solution


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # answer based on heap
        heap =[]
        for x,y in points:
            heapq.heappush(heap, (-x**2-y**2,x, y))
            # print(heap)
            if len(heap) >K:
                heapq.heappop(heap)
        
        # print(heap)
        res = []
        while K>0:
            p, x, y = heapq.heappop(heap)
            res.append([x,y])
            K-=1
        return res
        
    
        
        
        