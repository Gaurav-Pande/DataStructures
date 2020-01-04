# google phone interview
# In this phone interview I was given one question.
#
# Question: Write a function that takes a list L and returns a random sublist of size N of that list. Assume that the indexes must be in increasing order. That is, you cannot go backwards.
#
# Example:

# L = [1, 2, 3, 4, 5]
# N = 3

# [1,2,3],[1,3,4][1,4,5]

class Solution():
	def __init__(self):
		self.result = []
	def findSublist(self,nums,k):
		result = []
		for i in range(len(nums)-k+1):
			for j in range(i+1,len(nums)-k+3):
				for k in range(j+1,len(nums)):
					result.append([nums[i],nums[j],nums[k]])
		return result










if __name__ == '__main__':
	ob =  Solution()
	print(ob.findSublist([1,2,3,4,5],3))