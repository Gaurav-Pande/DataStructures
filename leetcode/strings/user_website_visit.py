# link: https://leetcode.com/problems/analyze-user-website-visit-pattern/

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        # define a heap to store the tuple of all three sorted with timesatmp
        
        heap = []
        for i in range(len(timestamp)):
            heapq.heappush(heap, (timestamp[i], website[i], username[i]))
        
        # make a dic of user nad the website they visite in timestamp order
        users = collections.defaultdict(list)
        
        while heap:
            time, website, user = heapq.heappop(heap)
            # print(user)
            users[user].append(website)
            
            
        # now we need to find the combination of 3 elemetnds for each users visited website list and see how many times it has appeard in other user list
        
        count = collections.defaultdict(int)
        result = tuple()
        maximum = 0
        
        
        
        
        for key, values in users.items():
            comb = itertools.combinations(values, 3)
            for seq in set(comb):
                count[seq] +=1
                if count[seq] > maximum:
                    maximum= count[seq]
                    result = seq
                elif count[seq]==maximum:
                    if seq < result:
                        result = seq
                        
        return list(result)
