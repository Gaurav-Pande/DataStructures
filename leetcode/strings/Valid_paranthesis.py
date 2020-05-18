#link: https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/162/

class Solution(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		def isalpha(char):
			return char.isalnum()

		def tolower(char):
			return char.lower()

		filtered_char = filter(isalpha, s)
		finalString = map(tolower, filtered_char)
		# print(finalString)

		return finalString == finalString[::-1]

