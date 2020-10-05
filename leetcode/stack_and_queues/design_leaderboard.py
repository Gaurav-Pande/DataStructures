#link: https://leetcode.com/problems/design-a-leaderboard/submissions/

class Leaderboard(object):

    def __init__(self):
        self.scores = collections.defaultdict(int)
        

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.scores[playerId] += score
        

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        result = sum(sorted(self.scores.values(), reverse =True)[:K])
        # print(sorted_scores)
        return result
        

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)




class Leaderboard(object):

    def __init__(self):
        self.scores = collections.defaultdict(int)
        

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.scores[playerId] += score
        

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        heap = []
        for score in self.scores.values():
            heapq.heappush(heap,score)
            if len(heap)>K:
                heapq.heappop(heap)
                
        return sum(heap)
        

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)