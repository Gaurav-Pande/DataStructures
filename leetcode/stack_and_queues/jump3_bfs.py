#link: https://leetcode.com/problems/jump-game-ii
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        # we can solve this question using bfs search method
        q =  collections.deque([start])
        seen = {start}
        
        while q:
            current = q.popleft()
            if arr[current] == 0:
                return True
            else:
                for child in current - arr[current], current+arr[current]:
                    if 0<=child<len(arr) and child not in seen:
                        seen.add(child)
                        q.append(child)
        return False