#[Longest Substring Without Repeating Characters](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = 1
        string = ""
        i = 0
        result = 0
        while i < len(s):
            j = i
            while j < j + window + 1 and j < len(s):
                if s[j] in string:
                    window = 1
                    string = ""
                    i = i + 1
                    j = i
                else:
                    string = string + s[j]
                    window = window + 1
                    result = max(result,len(string))
                    j = j + 1
                    
        return result
