# link: https://leetcode.com/problems/meeting-rooms-ii/

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        if not intervals:
            return 0
        
        si = sorted(intervals, key= lambda k:k[0])
        
        free_rooms = []
        
        heapq.heappush(free_rooms, si[0][1])
        
        for interval in si[1:]:
            if interval[0] >= free_rooms[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, interval[1])
            
        return len(free_rooms)

            
        
        
        
        
