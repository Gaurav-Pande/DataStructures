# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		## below solution is based on xor operation. let b be the different
		## number then
		## xor(0,b)=b
		## xor(a,a) = 0
		##

		a = 0
		for num in nums:
			a ^= num

		return a

## below is dictionary based implementation
#         dic = {}
#         for num in nums:
#             if num in dic:
#                 dic[num]+=1
#             else:
#                 dic[num] = 1

#         for k,v in dic.items():
#             if v == 1:
#                 return k

#         return 0