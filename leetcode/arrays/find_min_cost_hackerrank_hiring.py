"""
Given an array of integers, find the minimum cost to make the array either increasing or decreasing(not strictly).

Cost is defined as absolute difference of the old value of the element and the new value of the element.

Ex: 9 8 7 2 3 3
Minimum Cost: 1
In the above array, 4th element ‘2’ can be changed to ‘3’ to make the array decreasing. So cost = abs(3 - 2) = 1.

Ex: 10 6 3 2 2000
Minimum Cost: 11
1st element 10 can be changed to 6. Cost = abs(10 - 6) = 4.
3rd element 3 can be changed to 6. Cost = abs(3 - 6) = 3.
4th element 2 can be changed to 6. Cost = abs(2 - 6) = 4.
So total cost = 11

No. of elements: 10^4
Range of elements: [1, 10^9]

This question was asked in a contest(which is now over)
"""


def minCost(nums):
	indices = []
	for i in range(1,len(nums)):
		if i == len(nums)-1:
			
		if i+1<len(nums) and nums[i-1]<nums[i]<nums[i+1]:
			continue
		else:
			indices.append(i)
	print(indices)







nums = [9,8,7,2,2,3]
nums = [10,6,3,2,2000]
minCost(nums)