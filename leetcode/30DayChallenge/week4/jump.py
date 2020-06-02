# link:



# Backtracking solution TLE
class Solution(object):
    def __init__(self):
        self.memo = collections.defaultdict(bool)
    def canJump(self, nums):
        return self.backTracking(nums, 0)
    
    def backTracking(self, nums, pos):
        if pos == len(nums)-1:
            return True
        else:
            jump = min(pos+nums[pos],len(nums)-1)
            i=pos+1
            while i<=jump:
                if self.backTracking(nums,i):
                    return True
                i+=1
        return False

# With memoization  TLE
class Solution(object):
    def __init__(self):
        self.memo = []
    def canJump(self, nums):
        for i,v in enumerate(nums):
            self.memo.append("UNK")
        self.memo[len(nums)-1]= True
        #print(self.memo)
        res = self.backTracking(nums, 0)
        # print(self.memo)
        return res
    def backTracking(self, nums, pos):
        #print(pos, self.memo)
        if self.memo[pos] != "UNK":
            if self.memo[pos]:
                return True
            else:
                return False
        jump = min(pos+nums[pos],len(nums)-1)
        i=pos+1
        while i<=jump:
            if self.backTracking(nums,i):
                self.memo[i] = True
                return True
            i+=1
                
        self.memo[pos] = False
        return False
            
 # with DP TLE
 """
The observation to make here is that we only ever jump to the right. 
This means that if we start from the right of the array, 
every time we will query a position to our right, 
that position has already be determined as being GOOD or BAD. 
This means we don't need to recurse anymore, as we will always hit the memo table.
 """

class Solution(object):
    def canJump(self, nums):
        memo = []
        for i in range(0,len(nums)):
            memo.append("UNK")
        memo[len(nums)-1] = True
        print(memo)
        i= len(nums)-2
        while i >=0:
            jump = min(i + nums[i],len(nums)-1)
            j=i+1
            while j<=jump:
                if memo[j]==True:
                    memo[i]=True
                    break
                j+=1
            i-=1
        print(memo)
        if memo[0]==True:
            return True
        else:
            return False


# GREEDY ACCEPTED
class Solution(object):
    def canJump(self, nums):
        # initially we put the goal as last index
        # but we need to make goal=0
        # because once goal=0,it means we were successfully able to travese from right to index 0.
        goal = len(nums)-1
        for i in reversed(range(0,len(nums))):
            # traverse from rightmost side and check what is the max you can jump 
            max_jump = i+nums[i]
            # if the max jump is greater then the goal then from current i we can easily reach goal
            # then we make current index as goal as 
            if max_jump >= goal:
                goal = i
                
        # if finally we were able to reach the 0 index then return  true
        return goal == 0
        
        
                
            
        
            