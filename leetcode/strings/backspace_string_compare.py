# https://leetcode.com/problems/backspace-string-compare/
class Solution(object):
	def backspaceCompare(self, S, T):
		"""
		:type S: str
		:type T: str
		:rtype: bool
		"""
		stack1 = []
		stack2 = []
		for i in range(len(S)):
			stack1.append(S[i])
			if stack1[-1] == '#':
				stack1.pop()
				if not stack1:
					continue
				else:
					stack1.pop()

		for j in range(len(T)):
			stack2.append(T[j])
			if stack2[-1] == '#':
				stack2.pop()
				if not stack2:
					continue
				else:
					stack2.pop()

		# print(stack1)
		# print(stack2)
		if ''.join(stack1) == ''.join(stack2):
			return True
		else:
			return False
