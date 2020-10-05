# Author: Gaurav pande
# Question: 
"""

Given two strings, write a method to decide if one is a permutation of the
other.
• Ex) is_permutation(“eleven plus two”, “twelve plus one”) —> True
• is_permutation(“eat”, “tee”) —> False

"""

def is_permuation(s1, s2):
	"""
	s1: string
	s2: string
	return: True or False
	"""
	# we can get the ascii value for each charactor in the list and add it 
	ascii_s1, ascii_s2 = 0,0 
	if len(s1)!=len(s2) or not s1 or not s2: # O(1) 
		# handeling the edge cases, so that we wont waste time if one of the string is 
		# empty ot both of them doesnt contain equal number of chars
		return False

	for char in s1: # -> O(n)
		ascii_s1 += ord(char)

	for char in s2: # -> O(n)
		ascii_s2 += ord(char)

	if not abs(ascii_s1-ascii_s2): # O(1)
		return True
	else:
		return False



# Time complexity: O(n)
# space complexity = O(1)


# Summary:

"""

The general idea that I played along is that first what type of 2 strings are considered to be 
permutation. Some examples and assumption made along are as follow:
is_permutation(“eleven plus two”, “twelve plus one”) —> True 
is_permutation("ab cd", "c adb") -> True, which means space(" ") is considered to be in premuttaion
is_permutation(“eleven plus two”, “twelv eplus one”) —> True
is_permutaion("AbAb",aBaB) -> False, as both 'a' and 'A' are different chars
is_permutation("abx","adhakjda") -> False, length not equal
is_permuatation('@#$', '$#@') -> True, special chars are included in permuation

so if we considered all charactor, numbers, special chars to be included in our permutation
then following idea can work:

* walk through each string s1, and s2 char by char, find there ascii value and add them
* if they are permutaions then sum of there ascii value should be same, else they are not
permutaion
* compare the ascii sum of both string and return true if it is equal else false




"""