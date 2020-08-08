# link https://leetcode.com/problems/time-based-key-value-store/

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)
        self.latest = 0
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dic[key].append((value, timestamp))
        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        nums = self.dic[key]
        if not nums:
            return ""
        # we have to find largest timestamp which is smaller then or equal to given timestamp
        l,r=0,len(nums)
        # print(nums)
        while l<r:
            mid = (l+r)//2
            val, timestamp1 = nums[mid]
            #if we find the match then return immediately
            if timestamp1 == timestamp:
                return val
            # if the mid valus is smaller the asking timestamp then go further right
            elif timestamp1<timestamp:
                l = mid+1
            # otherwise if the mid value is larger then asking timestamp then we go to left
            # why we dont go left
            else:
                r = mid

        return "" if r ==0 else nums[r-1][0]
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)